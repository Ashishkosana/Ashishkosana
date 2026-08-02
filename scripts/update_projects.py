"""Regenerate the auto "All Projects" block in the profile README from GitHub.

Runs in a GitHub Action on a schedule. The curated "Featured Projects" table
above the markers is hand-maintained and never touched; this only rewrites the
block between <!--PROJECTS:START--> and <!--PROJECTS:END-->, so any new repo
with a description shows up automatically — no manual editing.
"""
from __future__ import annotations

import json
import os
import re
import urllib.request

USER = "Ashishkosana"
README = "README.md"
START = "<!--PROJECTS:START-->"
END = "<!--PROJECTS:END-->"

# Already highlighted in the hand-curated Featured table — skip to avoid dupes.
FEATURED = {"rythu", "review-lens", "career-copilot", "snip", "fastapi-saas-api"}
# Noise that shouldn't appear as a "project".
DENY = {USER.lower(), "ashishkosana.github.io", "url-preview-demo", "rythu-prototype"}


def repos():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def build_table():
    rows = []
    for r in repos():
        name = r["name"]
        if r.get("fork") or r.get("archived") or r.get("private"):
            continue
        if name.lower() in DENY or name.lower() in FEATURED:
            continue
        desc = (r.get("description") or "").strip()
        if not desc:  # a project worth showing has a description
            continue
        lang = r.get("language") or ""
        stars = r.get("stargazers_count", 0)
        meta = " · ".join(x for x in [lang, (f"⭐{stars}" if stars else "")] if x)
        rows.append(f"| **[{name}](https://github.com/{USER}/{name})** | {desc} "
                    f"{('<br>`' + meta + '`') if meta else ''} |")
    if not rows:
        return "_No additional projects yet._"
    header = "| Project | What it is |\n|---|---|\n"
    return header + "\n".join(rows)


def main():
    with open(README, encoding="utf-8") as f:
        text = f.read()
    block = f"{START}\n\n### 📦 More Projects\n\n_Auto-updated from my repos — newest first._\n\n{build_table()}\n\n{END}"
    if START in text and END in text:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    else:  # first run — append the block at the end
        new = text.rstrip() + "\n\n---\n\n" + block + "\n"
    if new != text:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new)
        print("README updated.")
    else:
        print("No change.")


if __name__ == "__main__":
    main()

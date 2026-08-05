# Hi, I'm Ashish Kosana 👋

**Software Engineer — Backend & Full-Stack.** I build products end to end — REST APIs, auth, payments, and cloud infrastructure, backed by tests and CI — and I use LLMs as an engineering tool, not as a specialty.

- 🔭 **Building:** [**Rythu**](https://main.d3jtg3gae71asa.amplifyapp.com) — a **live full-stack web app** (Next.js/TypeScript + Python/AWS serverless) · [review-lens](https://github.com/Ashishkosana/review-lens) — a self-verifying LLM code reviewer · [career-copilot](https://github.com/Ashishkosana/career-copilot) — a serverless job-search agent on AWS
- 🌱 **Now shipping with:** Next.js · TypeScript · React (see Rythu) + system design
- 🌐 **Portfolio:** [ashishkosana.com](https://ashishkosana.com)  ·  📫 ashishkosana@gmail.com
- 🎓 B.S. Computer Science, UMass Lowell (Dec 2025) · open to new-grad SWE / Backend / Full-Stack roles

---

### 🛠️ Tech

[![My Skills](https://skillicons.dev/icons?i=python,typescript,fastapi,nextjs,react,aws,dynamodb,postgres,docker,git,githubactions,linux,flutter,dart&perline=14)](https://ashishkosana.com)

**Backend:** REST API design · JWT / OAuth2 · hexagonal (ports & adapters) · SQLModel / SQLAlchemy · Stripe
**Cloud:** AWS Lambda · DynamoDB · API Gateway · Cognito · CDK (IaC) · EventBridge · Secrets Manager
**Quality:** pytest · mypy --strict · ruff · GitHub Actions · security review (OWASP Top 10)

---

### 🚀 Featured Projects

| Project | What it is |
|---|---|
| **[Rythu](https://main.d3jtg3gae71asa.amplifyapp.com)** · [code](https://github.com/Ashishkosana/rythu) | **Live full-stack app** for Telangana farmers — Next.js/TypeScript frontend + Python/AWS serverless backend (Lambda · DynamoDB · API Gateway · CDK). Honest, explainable, Telugu-first. |
| **[review-lens](https://github.com/Ashishkosana/review-lens)** | Automated code reviewer — runs an LLM across multiple lenses, then self-verifies each finding before flagging it (precision over recall). Python · CLI + GitHub Action · 80+ tests · eval harness. |
| **[career-copilot](https://github.com/Ashishkosana/career-copilot)** | Live serverless job-search agent on AWS — CDK-defined (Lambda · DynamoDB · API Gateway · Cognito). Triages Gmail, scores jobs, drafts replies with an LLM. |
| **[snip](https://github.com/Ashishkosana/snip)** | URL-shortener API from first principles — FastAPI + SQLModel, base62 codec, per-IP token-bucket rate limiting, Dockerized. |
| **[fastapi-saas-api](https://github.com/Ashishkosana/fastapi-saas-api)** | Multi-tenant SaaS API — JWT auth, per-user isolation, Stripe subscription webhooks, Postgres, Docker. |

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishkosana)
[![Website](https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=googlechrome&logoColor=white)](https://ashishkosana.com)
[![Resume](https://img.shields.io/badge/Resume-4285F4?style=flat-square&logo=readdotcv&logoColor=white)](https://ashishkosana.com/resume.pdf)

---

<!--PROJECTS:START-->

### 📦 More Projects

_Auto-updated from my repos — newest first._

| Project | What it is |
|---|---|
| **[jobs-mcp](https://github.com/Ashishkosana/jobs-mcp)** | An MCP server that gives any LLM live access to US software-engineering jobs — Greenhouse/Lever/Ashby + community feed, US-only, clearance-filtered, no API keys. <br>`Python` |
| **[resume-tailor](https://github.com/Ashishkosana/resume-tailor)** | Constraint-enforced resume tailoring that provably cannot fabricate — select/reorder/rephrase from a fact bank you wrote, verified before any PDF is written. <br>`Python` |
| **[deref](https://github.com/Ashishkosana/deref)** | A Zachtronics-style DSA game: write real Python, an execution-trace engine runs it, robots walk and a power meter browns out on slow code. Python engine + Flutter client. <br>`Python` |
| **[tick](https://github.com/Ashishkosana/tick)** | Durable job and cron scheduler on Postgres: SKIP LOCKED concurrent claiming, leases with crash recovery, retries with backoff, and a dead-letter state. <br>`Python` |
| **[ledgerline](https://github.com/Ashishkosana/ledgerline)** | Exactly-once payments service (Python/FastAPI/Postgres): storage-layer idempotency, double-entry ledger, transactional outbox, and dead-letter queue. <br>`Python` |
| **[sitepulse](https://github.com/Ashishkosana/sitepulse)** | Privacy-first web analytics: beacon to ingest to dashboard (FastAPI, deploys to Azure) <br>`Python` |
| **[agent-bus](https://github.com/Ashishkosana/agent-bus)** | A file-based coordination bus for running many AI coding-agent (or CLI) sessions in parallel — atomic flock claims, two-way inboxes, rollup. No server. <br>`Python` |
| **[askdocs-rag](https://github.com/Ashishkosana/askdocs-rag)** | Production RAG document Q&A with a retrieval + answer-quality evaluation harness (LLM, ChromaDB, FastAPI). <br>`Python` |
| **[data-analyst-agent](https://github.com/Ashishkosana/data-analyst-agent)** | Agentic SQL data-analyst: an LLM uses read-only SQL tool-calls to explore a database and answer questions. <br>`Python` |
| **[ai-clone](https://github.com/Ashishkosana/ai-clone)** | Chat-first personal site — talk to an AI clone that answers from a grounded knowledge base. AWS serverless: CDK, Lambda, DynamoDB, API Gateway, CloudFront. <br>`Python` |
| **[aws-serverless-cicd](https://github.com/Ashishkosana/aws-serverless-cicd)** | CI/CD pipeline for AWS serverless apps — GitHub Actions deploying CDK stacks (Lambda, API Gateway, DynamoDB) across dev/prod stages <br>`TypeScript` |
| **[envlint](https://github.com/Ashishkosana/envlint)** | Zero-dependency CLI that lints a .env file against a declared schema (required/type/duplicate/undeclared checks), CI-friendly exit codes <br>`Python` |
| **[streaming-analytics](https://github.com/Ashishkosana/streaming-analytics)** | Event-time windowed stream analytics: tumbling windows, watermarks, late-event handling, DuckDB sink <br>`Python` |
| **[retail-data-pipeline](https://github.com/Ashishkosana/retail-data-pipeline)** | Modern data-stack pipeline: synthetic data -> DuckDB -> dbt star schema + data-quality tests, with CI <br>`Python` |

<!--PROJECTS:END-->

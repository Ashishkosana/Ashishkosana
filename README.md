# Hi, I'm Ashish Kosana

**Software Engineer — Backend, Full-Stack & Systems.** I ship end-to-end products: APIs, auth, payments, and AWS serverless — with tests, CI, and the boring reliability details that keep money and jobs from double-firing. LLMs are a tool in the loop, not the product identity.

[![Website](https://img.shields.io/badge/ashishkosana.com-111111?style=flat-square&logo=googlechrome&logoColor=white)](https://www.ashishkosana.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishkosana)
[![Resume](https://img.shields.io/badge/Resume-PDF-4285F4?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://www.ashishkosana.com/resume.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Ashishkosana-181717?style=flat-square&logo=github)](https://github.com/Ashishkosana)

- **Building:** [Rythu](https://main.d3jtg3gae71asa.amplifyapp.com) (live full-stack) · [ledgerline](https://github.com/Ashishkosana/ledgerline) (exactly-once payments) · [agent-hands](https://github.com/Ashishkosana/agent-hands) (record-once / replay-many computer use)
- **Open source:** upstream feature in [getmoto/moto#10162](https://github.com/getmoto/moto/pull/10162) · recent review on [getmoto/moto#10234](https://github.com/getmoto/moto/pull/10234)
- **Stack focus:** Python · TypeScript/Next.js · FastAPI · Postgres · AWS (Lambda, DynamoDB, API Gateway, CDK) · GitHub Actions
- **Education:** B.S. Computer Science, UMass Lowell (Dec 2025) · open to new-grad SWE / Backend / Full-Stack
- **Contact:** ashishkosana@gmail.com

---

### Tech

[![Skills](https://skillicons.dev/icons?i=python,typescript,fastapi,nextjs,react,aws,dynamodb,postgres,docker,git,githubactions,linux,flutter,dart&perline=14)](https://www.ashishkosana.com/)

| Area | What I actually use |
| --- | --- |
| **Backend** | REST · JWT/OAuth2 · hexagonal ports & adapters · SQLModel/SQLAlchemy · idempotency & outbox patterns |
| **Cloud** | Lambda · DynamoDB · API Gateway · Cognito · CDK · EventBridge · Secrets Manager |
| **Quality** | pytest · mypy --strict · ruff · GitHub Actions · Dependabot · branch-protected `main` |
| **Product** | Flutter · Next.js · RAG eval harnesses · MCP servers |

---

### Featured work

| Project | What it proves | Status |
| --- | --- | --- |
| **[Rythu](https://main.d3jtg3gae71asa.amplifyapp.com)** · [code](https://github.com/Ashishkosana/rythu) | Live full-stack for Telangana farmers — Next.js + Python/AWS serverless (Lambda · DynamoDB · API Gateway · CDK) | [![CI](https://github.com/Ashishkosana/rythu/actions/workflows/ci.yml/badge.svg)](https://github.com/Ashishkosana/rythu/actions) · [v0.1.0](https://github.com/Ashishkosana/rythu/releases/tag/v0.1.0) |
| **[ledgerline](https://github.com/Ashishkosana/ledgerline)** | Exactly-once payments — storage-layer idempotency, double-entry ledger, transactional outbox, DLQ | [v0.1.0](https://github.com/Ashishkosana/ledgerline/releases/tag/v0.1.0) |
| **[tick](https://github.com/Ashishkosana/tick)** | Durable Postgres job/cron scheduler — `SKIP LOCKED`, leases, retries, dead-letter | [v0.1.0](https://github.com/Ashishkosana/tick/releases/tag/v0.1.0) |
| **[agent-hands](https://github.com/Ashishkosana/agent-hands)** | Record-once / replay-many computer-use — typed capability artifact, no model in the replay loop | [![CI](https://github.com/Ashishkosana/agent-hands/actions/workflows/ci.yml/badge.svg)](https://github.com/Ashishkosana/agent-hands/actions) · [v0.1.0](https://github.com/Ashishkosana/agent-hands/releases/tag/v0.1.0) |
| **[review-lens](https://github.com/Ashishkosana/review-lens)** | Multi-lens LLM code review with adversarial self-verification (precision over recall) | [![CI](https://github.com/Ashishkosana/review-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/Ashishkosana/review-lens/actions) · [v0.1.0](https://github.com/Ashishkosana/review-lens/releases/tag/v0.1.0) |
| **[deref](https://github.com/Ashishkosana/deref)** | Zachtronics-style DSA game — real Python + execution-trace engine + Flutter client | [v0.1.0](https://github.com/Ashishkosana/deref/releases/tag/v0.1.0) |
| **[askdocs-rag](https://github.com/Ashishkosana/askdocs-rag)** | Production RAG Q&A with retrieval + answer-quality evaluation harness | [![CI](https://github.com/Ashishkosana/askdocs-rag/actions/workflows/ci.yml/badge.svg)](https://github.com/Ashishkosana/askdocs-rag/actions) · [v0.1.0](https://github.com/Ashishkosana/askdocs-rag/releases/tag/v0.1.0) |
| **[jobs-mcp](https://github.com/Ashishkosana/jobs-mcp)** | MCP server — live US SWE jobs from Greenhouse/Lever/Ashby (no API keys) | [v0.1.0](https://github.com/Ashishkosana/jobs-mcp/releases/tag/v0.1.0) |

**How I work on GitHub:** MIT on public heroes · Dependabot · protected `main` · Releases · Actions CI on shipping repos · real upstream PRs and reviews — not just a dump of coursework.

---

<!--PROJECTS:START-->

### 📦 More Projects

_Auto-updated from my repos — newest first._

| Project | What it is |
|---|---|
| **[OS-Data-Structures-Learning](https://github.com/Ashishkosana/OS-Data-Structures-Learning)** | Learn data structures by visually studying how they're actually used in a real OS (Linux kernel). Annotated code examples and explanations. <br>`Python` |
| **[agent-hands](https://github.com/Ashishkosana/agent-hands)** | Record-once / replay-many computer-use automation: an LLM discovers a UI flow once; a typed capability artifact replays it deterministically with no model in the loop. <br>`Python · ⭐1` |
| **[tick](https://github.com/Ashishkosana/tick)** | Durable job and cron scheduler on Postgres: SKIP LOCKED concurrent claiming, leases with crash recovery, retries with backoff, and a dead-letter state. <br>`Python` |
| **[ledgerline](https://github.com/Ashishkosana/ledgerline)** | Exactly-once payments service (Python/FastAPI/Postgres): storage-layer idempotency, double-entry ledger, transactional outbox, and dead-letter queue. <br>`Python` |
| **[event-worker-agent](https://github.com/Ashishkosana/event-worker-agent)** | Event-driven worker agent: queue claim → tool calls → DLQ + backoff. Portfolio scaffold (honest queue/worker signal). <br>`Python` |
| **[ide-pair-agent](https://github.com/Ashishkosana/ide-pair-agent)** | Flagship: VS Code extension + local pair agent that relays editor context to a desktop assistant (Grok Bot) via webhook/mailbox — honest portfolio, YOU IMPLEMENT on the agent loop <br>`Python` |
| **[ops-agent](https://github.com/Ashishkosana/ops-agent)** | Multi-tool coding/ops agent with hard evals: planner → tools → verifier → scorecard (CLI + GitHub Action). Portfolio scaffold. <br>`Python` |
| **[vendor-orchestrator](https://github.com/Ashishkosana/vendor-orchestrator)** | Vendor orchestration agent: FastAPI case service → mock vendors → retries/idempotency → Postgres case state → eval harness (portfolio; honest mock metrics only) <br>`Python` |
| **[deref](https://github.com/Ashishkosana/deref)** | A Zachtronics-style DSA game: write real Python, an execution-trace engine runs it, robots walk and a power meter browns out on slow code. Python engine + Flutter client. <br>`Python` |
| **[jobs-mcp](https://github.com/Ashishkosana/jobs-mcp)** | An MCP server that gives any LLM live access to US software-engineering jobs — Greenhouse/Lever/Ashby + community feed, US-only, clearance-filtered, no API keys. <br>`Python` |
| **[askdocs-rag](https://github.com/Ashishkosana/askdocs-rag)** | Production RAG document Q&A with a retrieval + answer-quality evaluation harness (LLM, ChromaDB, FastAPI). <br>`Python` |
| **[resume-tailor](https://github.com/Ashishkosana/resume-tailor)** | Constraint-enforced resume tailoring that provably cannot fabricate — select/reorder/rephrase from a fact bank you wrote, verified before any PDF is written. <br>`Python` |
| **[job-search-agents](https://github.com/Ashishkosana/job-search-agents)** | Job-search agents + a sourcing pipeline that only surfaces roles genuinely posted in the last few days — reads the employer's first-publish date (not the repost date), the real years bar from the JD body, and your own mailbox for duplicates. Human submits. <br>`Python` |
| **[agent-bus](https://github.com/Ashishkosana/agent-bus)** | A file-based coordination bus for running many AI coding-agent (or CLI) sessions in parallel — atomic flock claims, two-way inboxes, rollup. No server. <br>`Python` |
| **[data-analyst-agent](https://github.com/Ashishkosana/data-analyst-agent)** | Agentic SQL data-analyst: an LLM uses read-only SQL tool-calls to explore a database and answer questions. <br>`Python` |
| **[ai-clone](https://github.com/Ashishkosana/ai-clone)** | Chat-first personal site — talk to an AI clone that answers from a grounded knowledge base. AWS serverless: CDK, Lambda, DynamoDB, API Gateway, CloudFront. <br>`Python` |
| **[aws-serverless-cicd](https://github.com/Ashishkosana/aws-serverless-cicd)** | CI/CD pipeline for AWS serverless apps — GitHub Actions deploying CDK stacks (Lambda, API Gateway, DynamoDB) across dev/prod stages <br>`TypeScript` |
| **[envlint](https://github.com/Ashishkosana/envlint)** | Zero-dependency CLI that lints a .env file against a declared schema (required/type/duplicate/undeclared checks), CI-friendly exit codes <br>`Python` |
| **[streaming-analytics](https://github.com/Ashishkosana/streaming-analytics)** | Event-time windowed stream analytics: tumbling windows, watermarks, late-event handling, DuckDB sink <br>`Python` |
| **[retail-data-pipeline](https://github.com/Ashishkosana/retail-data-pipeline)** | Modern data-stack pipeline: synthetic data -> DuckDB -> dbt star schema + data-quality tests, with CI <br>`Python` |

<!--PROJECTS:END-->

---

### Elsewhere

[ashishkosana.com](https://www.ashishkosana.com/) · [LinkedIn](https://www.linkedin.com/in/ashishkosana) · [Resume (PDF)](https://www.ashishkosana.com/resume.pdf) · ashishkosana@gmail.com

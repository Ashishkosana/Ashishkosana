<!-- GitHub profile README: https://github.com/Ashishkosana -->

# Hi, I'm Ashish Kosana

**Backend & Distributed Systems · Applied AI.** Seeking software engineer roles. Authorized to work in the U.S. on F-1 OPT — STEM, ~3 years, no sponsorship needed to start.

I build APIs, PostgreSQL-backed workers, and event pipelines that stay correct under retries, crashes, and concurrent claimants. When a model is in the loop, I put policy, metering, and evaluation in front of it — not a chat wrapper.

[![Website](https://img.shields.io/badge/ashishkosana.com-111111?style=flat-square&logo=googlechrome&logoColor=white)](https://www.ashishkosana.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishkosana)
[![Resume](https://img.shields.io/badge/Resume-PDF-4285F4?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://www.ashishkosana.com/resume.pdf)

- **Now:** Software Engineer Intern at Crewtron / Augment AI Labs (Flutter client + AWS serverless backend)
- **Flagship:** [autonomous-agent](https://github.com/Ashishkosana/autonomous-agent) · [agent-hands](https://github.com/Ashishkosana/agent-hands)
- **Live:** [Ask Ashish](https://www.ashishkosana.com/) on ashishkosana.com · [jobs.ashishkosana.com](https://jobs.ashishkosana.com)
- **Open source:** merged [`get_tags` for API Gateway stages](https://github.com/getmoto/moto/pull/10162) in [moto](https://github.com/getmoto/moto)
- **Stack:** Python · FastAPI · PostgreSQL · TypeScript/Next.js · AWS (Lambda, DynamoDB, API Gateway, CDK)
- **Education:** B.S. Computer Science, UMass Lowell (Dec 2025)

---

## Featured engineering work

[autonomous-agent](https://github.com/Ashishkosana/autonomous-agent) and [agent-hands](https://github.com/Ashishkosana/agent-hands) first. [platform-forge](https://github.com/Ashishkosana/platform-forge), [realtime-event-platform](https://github.com/Ashishkosana/realtime-event-platform), and [ai-reliability-control-plane](https://github.com/Ashishkosana/ai-reliability-control-plane) include failure drills (crash, poison, races) and architecture notes.

| Project | Engineering focus |
| --- | --- |
| **[autonomous-agent](https://github.com/Ashishkosana/autonomous-agent)** | One high-level goal. Plans and acts inside an isolated Linux sandbox, checks the result against mechanical criteria, and can retrieve those records on a later run. Model weights stay fixed. |
| **[agent-hands](https://github.com/Ashishkosana/agent-hands)** | Record once, replay many. A model discovers a UI flow once; a typed capability artifact replays it with no model in the loop. An unobservable consequential outcome ends as `UNRESOLVED`. |
| **[platform-forge](https://github.com/Ashishkosana/platform-forge)** | Durable linear workflows on PostgreSQL. Workers claim steps with `FOR UPDATE SKIP LOCKED`, heartbeat a lease, and a fencing token rejects zombie commits. Retries use full jitter, then dead-letter. |
| **[realtime-event-platform](https://github.com/Ashishkosana/realtime-event-platform)** | Persist-first notifications. Idempotent ingest, transactional fan-out into a per-user inbox, SSE catch-up by cursor, at-least-once webhooks with leases, backoff, dead-letter, and HMAC signatures. |
| **[ai-reliability-control-plane](https://github.com/Ashishkosana/ai-reliability-control-plane)** | A `complete()` control plane. Atomic SQL tenant budgets, kill switch, fail-closed if the store is down, one retry then fallback, immutable prompt versions, promote blocked unless a golden eval passes. |
| **[ledgerline](https://github.com/Ashishkosana/ledgerline)** | Payments that stay consistent under retry. UNIQUE idempotency key, payment state machine, double-entry ledger, transactional outbox, consumer inbox dedup, then DLQ. |

**Also:** [Rythu](https://github.com/Ashishkosana/rythu) — Telugu-first weather and crop advisory (Next.js + Python on AWS) · [review-lens](https://github.com/Ashishkosana/review-lens) — LLM review, then a refutation pass against the diff. Suggests; never auto-applies.

---

## Engineering focus

- **Postgres as a concurrency primitive** — skip-locked claims, leases, fencing, inspectable state. No broker required for V1 of the systems work.
- **Delivery is a database problem first** — write the inbox, then stream or webhook. A dead socket must not be the source of truth.
- **Retries need a unique key** — uniqueness constraints and outbox/inbox pairs, not slogans about exactly-once.
- **Model calls are metered and gated** — budgets, kill switches, versioned prompts, eval that can refuse a promote.

---

## Open source

- Merged: [getmoto/moto#10162](https://github.com/getmoto/moto/pull/10162) — `get_tags` for API Gateway stages (completes the existing tag/untag pair).
- Review: [getmoto/moto#10234](https://github.com/getmoto/moto/pull/10234) — SQS `PurgeQueueInProgress` when a queue is purged twice within 60 seconds.

---

## Contact

[ashishkosana.com](https://www.ashishkosana.com/) · [LinkedIn](https://www.linkedin.com/in/ashishkosana) · [Resume (PDF)](https://www.ashishkosana.com/resume.pdf) · ashishkosana@gmail.com

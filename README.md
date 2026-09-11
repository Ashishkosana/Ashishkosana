<!-- GitHub profile README: https://github.com/Ashishkosana -->

# Hi, I'm Ashish Kosana

**Software Engineer** focused on backend, distributed systems, and full-stack product engineering.

I build APIs, PostgreSQL-backed workers, and event pipelines that stay correct under retries, crashes, and concurrent claimants. When a model is in the loop, I put policy, metering, and evaluation in front of it — not a chat wrapper.

[![Website](https://img.shields.io/badge/ashishkosana.com-111111?style=flat-square&logo=googlechrome&logoColor=white)](https://www.ashishkosana.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishkosana)
[![Resume](https://img.shields.io/badge/Resume-PDF-4285F4?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://www.ashishkosana.com/resume.pdf)

- **Now:** Software Engineer Intern at Crewtron / Augment AI Labs (Flutter client + AWS serverless backend)
- **Shipped:** [Rythu](https://github.com/Ashishkosana/rythu) — Telugu-first weather and crop advisory (Next.js + Python on AWS)
- **Open source:** merged [`get_tags` for API Gateway stages](https://github.com/getmoto/moto/pull/10162) in [moto](https://github.com/getmoto/moto)
- **Stack:** Python · FastAPI · PostgreSQL · TypeScript/Next.js · AWS (Lambda, DynamoDB, API Gateway, CDK)
- **Education:** B.S. Computer Science, UMass Lowell (Dec 2025)
- **Seeking:** Software Engineer / SDE roles — backend, systems, full-stack

---

## Featured engineering work

Six projects. Different problems. What the code actually does:

| Project | Engineering focus |
| --- | --- |
| **[platform-forge](https://github.com/Ashishkosana/platform-forge)** | Durable linear workflows on PostgreSQL. Workers claim steps with `FOR UPDATE SKIP LOCKED`, heartbeat a lease, and a fencing token rejects zombie commits. Retries use full jitter, then dead-letter. **At-least-once** steps; idempotent side effects only if the handler uses the key. |
| **[realtime-event-platform](https://github.com/Ashishkosana/realtime-event-platform)** | Persist-first notifications. Idempotent ingest, transactional fan-out into a per-user inbox (chunked when the recipient list is large), SSE catch-up by cursor, **at-least-once** webhooks with leases, backoff, dead-letter, and HMAC signatures. The event id is the consumer’s idempotency token. |
| **[ai-reliability-control-plane](https://github.com/Ashishkosana/ai-reliability-control-plane)** | A `complete()` control plane, not a chatbot. Atomic SQL tenant budgets, kill switch, fail-closed if the store is down, one retry then fallback (timeouts do not fall back), immutable prompt versions, promote blocked unless a golden eval passes. V1 uses a fake provider so the policy path is testable. |
| **[Rythu](https://github.com/Ashishkosana/rythu)** | Shipped product: Telugu-first weather + crop-advisory PWA. Next.js on Amplify, hexagonal Python Lambda, DynamoDB TTL forecast cache, CDK. Weather is the live backend; crops, fertilizer calc, and schemes ship as client data. |
| **[ledgerline](https://github.com/Ashishkosana/ledgerline)** | Payments that stay consistent under retry. UNIQUE idempotency key (concurrent duplicates create one payment), payment state machine, double-entry ledger, transactional outbox, consumer inbox dedup, then DLQ. Not a global exactly-once bus — storage uniqueness plus outbox/inbox. |
| **[review-lens](https://github.com/Ashishkosana/review-lens)** | LLM code review across correctness, security, performance, and tests, then a refutation pass against the actual diff. Eval harness for precision/recall; GitHub Action posts comments. Suggests; never auto-applies. |

The three systems repos include failure drills (crash, poison, races) and architecture notes. Click those first in an interview.

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

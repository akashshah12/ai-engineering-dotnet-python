# AI System Design – End-to-End View

This module explains how **real-world AI systems** are designed
beyond simple model calls.

## Typical Architecture

Data
 → Processing (Python)
 → Model / LLM
 → Retrieval (Vector DB)
 → API / Orchestration (.NET)
 → Observability

## Why this matters
Most AI POCs fail because:
- data pipelines are ignored
- APIs are an afterthought
- cost and latency are not measured
- failures are invisible

## Python vs .NET responsibilities

### Python
- Data ingestion
- Feature extraction
- Embeddings
- Experimentation

### .NET
- APIs
- Authentication
- Rate limiting
- Caching
- Integration with enterprise systems

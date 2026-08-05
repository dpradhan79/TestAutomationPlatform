# ADR-003 PGVector Storage Strategy

## Status

Accepted

## Date

2026-08-05

## Context

The platform requires persistent storage for:

- Agent memory
- LangGraph checkpoints
- KnowledgeAgent indexing
- RAG retrieval
- Request history
- Evaluation results
- Application metadata

A storage strategy is required that can support both relational data and vector search.

## Options Considered

### Option 1

PostgreSQL Only

### Option 2

PostgreSQL + Separate Vector Database

Examples:

- Chroma
- Pinecone
- Qdrant

### Option 3

PostgreSQL + PGVector

## Decision

Use PostgreSQL with PGVector extension.

## Rationale

PGVector supports:

- Relational data
- JSON documents
- Vector embeddings

using a single platform.

This reduces:

- Infrastructure complexity
- Operational overhead
- Future migration effort

## Future Usage

### Checkpoints

LangGraph checkpoints

### Memory

Agent memory

### KnowledgeAgent

Knowledge indexing and retrieval

### Evaluation

Evaluation result storage

## Consequences

### Pros

- Single datastore
- Cloud friendly
- Azure compatible
- Supports RAG
- Supports semantic memory

### Cons

- Vector retrieval performance may not match highly specialized vector databases at very large scale

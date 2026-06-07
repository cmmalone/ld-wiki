# Context Compaction

## Overview
A mechanism used by long-running agent systems (such as Claude Code) to handle context window limits. When the conversation history approaches capacity, the agent generates a structured summary of what has happened, replaces the full history with that summary, and continues from there. This enables arbitrarily long sessions at the cost of some information loss.

## Across Episodes
- **S2E4**: S2E4 explains compaction mechanics in detail — including what gets preserved (high-level decisions, task state, next steps) and what gets lost (specific reasoning, subtle constraints) — and introduces CLAUDE.md as a mechanism to pin information that must survive compaction. → episodes/S2E4.md

## How our thinking has evolved
*(More episodes needed to identify trends.)*

## Related Concepts
*(To be linked as the wiki grows.)*

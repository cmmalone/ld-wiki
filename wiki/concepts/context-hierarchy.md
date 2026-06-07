# Context Hierarchy

## Overview
The structured layering of content within an LLM agent's context window, where different layers carry different levels of durability and implicit priority. Typically: system prompt (highest, set by the agent builder) → pinned project instructions (e.g. CLAUDE.md) → live conversation history (most dynamic, most vulnerable to loss). Position in the window and deliberate re-injection determine how reliably the model attends to each layer.

## Across Episodes
- **S2E4**: S2E4 presents the context hierarchy as a deliberate engineering response to the lost-in-the-middle finding: designers put critical information at the start of the context and re-inject it after compaction, working with the model's positional attention bias rather than against it. → episodes/S2E4.md

## How our thinking has evolved
*(More episodes needed to identify trends.)*

## Related Concepts
*(To be linked as the wiki grows.)*

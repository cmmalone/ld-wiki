# Error Propagation in Agentic Systems

## Overview
When an AI agent makes a mistake at one step, it corrupts the world state that all subsequent steps operate on. Because the agent typically has no ground truth to compare against, it continues reasoning from the mistaken state, often compounding errors invisibly until much later in the task.

## Across Episodes
- **S2E6**: S2E6 contrasts this with chatbot interactions, where a user can immediately catch and correct a wrong turn. In agents, the root cause of a failure ten steps in the future may be a mistake made early on that was never surfaced. → episodes/S2E6.md

## How our thinking has evolved
*(More episodes needed to identify trends.)*

## Related Concepts
*(To be linked as the wiki grows.)*

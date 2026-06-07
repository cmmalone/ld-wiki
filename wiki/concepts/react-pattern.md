# ReAct Pattern (Reasoning + Acting)

## Overview
ReAct is an architecture for AI agents that interleaves reasoning traces with real-world actions in a repeating loop: the model thinks about what to do, takes an action, observes the result, and uses that observation to inform its next thought. Introduced in a 2022 Google Research paper, it showed that combining reasoning and acting beats either approach alone. The pattern is foundational to most modern agent designs.

## Across Episodes
- **S2E2**: S2E2 walks through a worked HotpotQA example showing how ReAct's think–act–observe loop correctly answers a multi-hop question that both chain-of-thought-only and action-only approaches get wrong, and highlights that the loop's trajectory is interpretable for debugging. → episodes/S2E2.md

## How our thinking has evolved
*(More episodes needed to identify trends.)*

## Related Concepts
*(To be linked as the wiki grows.)*

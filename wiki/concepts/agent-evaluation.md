# Agent Evaluation

## Overview
Agent evaluation is the challenge of measuring how well an AI agent performs on complex, multi-step tasks that branch based on real-world feedback. Unlike single-turn LLM evaluation (compare output to a gold answer), agent evaluation must account for long action sequences, partial successes, irreversible mistakes, and emergent behaviors. It is an open research and engineering problem with three distinct sub-challenges: the world change problem, the long horizon credit assignment problem, and the question of what counts as success.

## Across Episodes
- **S2E1**: Flags agent evaluation as a forthcoming dedicated episode, noting that agents are 'complex and tricky to evaluate' precisely because of the consequences and branching inherent in the observe-reason-act loop. → episodes/S2E1.md
- **S2E7**: Organizes the agent evaluation problem into three distinct challenges: the world change problem (agents alter environments in ways that complicate measurement), the long horizon credit assignment problem (determining which actions in a long sequence deserve credit or blame), and the 'what counts as success' problem. Argues that most successful benchmarks have sidestepped rather than solved the third challenge, with significant consequences for which capabilities get developed. → episodes/S2E7.md

## How our thinking has evolved
- The framing has sharpened from a general acknowledgment that agent evaluation is hard (S2E1) to a structured decomposition of *why* it is hard (S2E7). The identification of the 'what counts as success' problem as the deepest and most consequential challenge — and the observation that benchmarks tend to avoid rather than resolve it — suggests that progress on agent capabilities may be systematically distorted by the evaluation tools we have chosen to rely on.

## Related Concepts
*(To be linked as the wiki grows.)*
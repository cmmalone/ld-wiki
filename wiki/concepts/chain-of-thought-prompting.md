# Chain-of-Thought Prompting

## Overview
Chain-of-thought prompting is a technique where a language model is instructed to reason step by step before producing a final answer, externalizing its intermediate reasoning process. It was shown to unlock significant latent capability in large models on tasks like math, logic, and professional exams. However, the reasoning it produces is grounded only in the model's training data, not in real-time external information, and is constrained to a single linear reasoning path with no ability to branch or backtrack.

## Across Episodes
- **S2E2**: Uses chain-of-thought as a baseline to motivate ReAct: chain-of-thought alone still hallucinated the wrong answer to the HotpotQA example because it could not verify its reasoning against the real world. → episodes/S2E2.md
- **S2E5**: Framed as a meaningful improvement over raw generation but with a structural limitation: it commits to a single linear path with no branching or backtracking, making it fundamentally unsuited to combinatorial search problems like Game of 24. → episodes/S2E5.md

## How our thinking has evolved
Chain-of-thought prompting has appeared across episodes primarily as a stepping stone that motivates more advanced techniques. S2E2 identified its grounding problem — it cannot verify claims against the real world — while S2E5 identified a structural problem orthogonal to grounding: even when reasoning from correct information, the linear, non-branching nature of chain-of-thought makes it ill-suited for problems that require exploration of multiple paths. Together, these episodes paint chain-of-thought as a capable but architecturally limited baseline, with each limitation motivating a distinct class of extensions (grounded reasoning in S2E2, tree-structured search in S2E5).

## Related Concepts
*(To be linked as the wiki grows.)*
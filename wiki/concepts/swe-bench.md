# SWE-bench

## Overview
SWE-bench is a benchmark for evaluating AI coding agents on real-world software engineering tasks drawn from GitHub issues. It measures whether an agent can resolve an issue by making the right code changes, verified by the repository's existing test suite. SWE-bench Verified is a curated subset intended to filter out ambiguous or poorly-specified tasks.

## Across Episodes
- **S2E6**: S2E6 traces SWE-bench Verified performance from ~2% (Claude 2, 2023) to ~94% (early 2026), while noting SWE-bench Mobile scores for the same frontier models are only ~12%, illustrating how benchmark scope dramatically changes the performance picture. → episodes/S2E6.md
- **S2E7**: S2E7 highlights SWE-bench as the primary evidence for dramatic coding agent progress (under 2% in 2023 to over 80% in 2025), but also as a cautionary tale: a 2026 OpenAI audit found roughly 60% of the hardest tasks had tests that would pass even without fixing the underlying bug, causing OpenAI to withdraw from the benchmark. → episodes/S2E7.md

## How our thinking has evolved
SWE-bench Verified initially served as a compelling indicator of rapid coding agent progress, with scores rising from roughly 2% in 2023 to well above 80% by 2025–2026. However, two complications have emerged across episodes: first, benchmark scope matters enormously—scores on SWE-bench Mobile for the same frontier models sit around 12%, a stark reminder that strong performance on one benchmark variant does not generalize automatically. Second, benchmark integrity has come into question, with an OpenAI audit finding that a substantial fraction of the hardest tasks had tests that could pass without actually fixing the underlying bug, leading OpenAI to withdraw from the benchmark entirely. Together, these episodes suggest that headline SWE-bench numbers require careful scrutiny of both what domain is being tested and whether the evaluation mechanism itself is sound.

## Related Concepts
*(To be linked as the wiki grows.)*
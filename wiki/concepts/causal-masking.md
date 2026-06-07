# Causal Masking

## Overview
A deliberate architectural feature of autoregressive transformer models where each token can only attend to tokens that appear before it in the sequence, not after. This enforces left-to-right processing and is necessary for the model to generate text one token at a time without 'seeing the future.'

## Across Episodes
- **S2E3**: S2E3 identifies causal masking as the primary architectural explanation for position bias: early tokens sit on far more attention pathways than middle tokens, giving them disproportionate influence — a result proven mathematically by the 2025 MIT paper. → episodes/S2E3.md

## How our thinking has evolved
*(More episodes needed to identify trends.)*

## Related Concepts
*(To be linked as the wiki grows.)*

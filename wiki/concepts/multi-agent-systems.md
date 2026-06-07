## Multi-Agent Systems

## Overview
Multi-agent systems involve multiple AI agents operating together — communicating, coordinating, and dividing work to accomplish tasks that a single agent might struggle with alone. Agents in such systems may have specialized roles, check each other's work, or operate in parallel. Coordination between agents introduces new challenges around consistency, communication overhead, and failure propagation. Empirical work suggests the benefits of multi-agent architectures are real but narrow, most clearly demonstrated on tasks that are genuinely parallelizable and that fall below roughly a 45% single-agent success threshold.

## Across Episodes
- **S2E1**: S2E1 briefly names multi-agent systems as one of the season's planned topics, framing it as a natural extension of single-agent complexity once the fundamentals are established. → episodes/S2E1.md
- **S2E8**: S2E8 uses multi-agent systems as its central subject, examining two papers that probe whether the added complexity actually improves outcomes over a single well-equipped agent. The episode concludes that multi-agent value is real but narrow, limited to genuinely parallelizable tasks below a ~45% single-agent success threshold. → episodes/S2E8.md

## How our thinking has evolved
Early in the season, multi-agent systems were treated as a promising but largely theoretical extension of single-agent work. By S2E8, empirical research had sharpened that picture considerably: multi-agent coordination does offer gains, but those gains are conditional. The architecture earns its complexity only when tasks can be meaningfully parallelized and when a single agent is already struggling — roughly below a 45% success rate. Above that threshold, or for tasks that resist parallelization, the overhead of coordination appears to outweigh the benefits.

## Related Concepts
*(To be linked as the wiki grows.)*
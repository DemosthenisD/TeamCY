---
name: actuarial-guide
description: Reference knowledge from "Claude Code for Actuaries — The Complete Guide" (Nzati & Schraub, 2026). Use for actuarial work with Claude Code — life/annuities (ALM, bonds, RBC, ORSA, reserves, VBA), P&C (GLM pricing, Chain Ladder/BF/Mack reserving), reinsurance (XL pricing, program optimization, Schedule F), actuarial CLAUDE.md files, prompt patterns, data-quality pipelines, Python-to-R migration, building actuarial AI agents, or AI governance for insurers.
---

# Actuarial guide

The guide is stored at `knowledge/claude-code-for-actuaries/`. Do not load it all.

1. Start with `knowledge/claude-code-for-actuaries/README.md` (summary) and `use-case-catalog.md` (use case → chapter file).
2. Read only the chapter file you need from `knowledge/claude-code-for-actuaries/chapters/`. Each use case contains a tested ready-to-adapt prompt with expected inputs/outputs.
3. For formulas or screenshots, check the PDF page (`Claude_Code_for_Actuaries_The_Complete_Guide.pdf`); the text extraction is approximate.
4. Companion datasets are not in the repo; links are in `companion-packs.md`.
5. For a new actuarial project, start from `claude-md-template-actuaries.md`.

When applying a use-case prompt: keep the guide's rules — synthetic data only unless the user states the data is approved, no secrets in code, propose architecture before large modules, write tests with the code, document assumptions, and flag anything needing actuarial validation. The actuary stays accountable; the guide is a starting point, not a substitute for professional judgment or regulatory compliance.

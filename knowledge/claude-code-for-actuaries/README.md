# Claude Code for Actuaries — The Complete Guide (knowledge base)

Source: *Claude Code for Actuaries — The Complete Guide* (62 pp, 2026), Ethel Cédric Nzati, AQ & David Schraub, FSA, CERA, MAAA, AQ. © 2026 Necflow AI & David Schraub Actuarial Consultancy. All rights reserved. Kept here as a private reference copy for agent use.

## Files

| File | Use |
|---|---|
| `Claude_Code_for_Actuaries_The_Complete_Guide.pdf` | Original (screenshots, formulas rendered) |
| `full-guide.txt` | Whole guide as text, `\f` between pages (page N = Nth form-feed block) |
| `chapters/NN-*.txt` | One file per chapter; agents should read only the chapter they need |
| `claude-md-template-actuaries.md` | The appendix CLAUDE.md template, ready to copy into an actuarial project |
| `companion-packs.md` | Index of the 10 downloadable project packs (Google Drive links) |
| `use-case-catalog.md` | The 32 use cases mapped to chapter file and practice area |

Text is `pdftotext -layout` output: tables/formulas are approximate. Check the PDF for formulas (e.g. the bond MV formula in ch. 5.1).

## What the guide says (summary)

**Thesis.** Claude Code is an agent, not a chat: it runs code, reads its own errors and self-corrects (autonomy), reads whole model folders (local access), and produces deliverables end to end. Three levels of use: (1) code generation, (2) project understanding, (3) workflow automation (one instruction runs a reproducible pipeline).

**Scope.** Life & annuities (ch. 5, use cases 1–23), P&C (ch. 6, 24–29), reinsurance (ch. 7, 30–32), internal tools in a day (ch. 8), agents (ch. 9). Each use case = business situation, what Claude will design, an exhaustive ready-to-paste prompt, expected inputs/outputs. Ten use cases ship with companion packs (dataset + CLAUDE.md + PROMPT.md + reference results).

**Setup (ch. 3).** Desktop app, Claude Pro is enough. Security before starting: scope the trusted folder to the project only; switch off "Help improve our AI models" on individual plans. Pack routine: download folder, point Claude Code at it, trust workspace, pick model/effort, attach PROMPT.md and say "run these instructions please", review permission requests. Keep CLAUDE.md under 200 lines, as an index to detailed files. MCP connectors come later ("a good CLAUDE.md already gives 80% of the value").

**Beyond code (ch. 4).** Spec review, gap detection, test plans, legacy VBA explanation, VBA→Python/R conversion, LaTeX documentation, decks, README, architecture, optimisation, code review.

**Internal tools (ch. 8).** ALM dashboard, RBC calculator, ORSA orchestrator, validation tool, data-quality tool, statutory report generator, Streamlit front-ends: prototypes in a day, can go to production if tested.

**Agents (ch. 9).** (a) Q&A agent over all functional specs, citing passages and saying so when absent; (b) agent over a team's codebase that explains what is really implemented and flags code-vs-spec gaps, citing files/lines; (c) monitoring, reporting and control agents. The agent prepares, proposes, alerts; the actuary validates.

**Governance (ch. 10).** Confidentiality terms are set by the company's IT/compliance, not the book. Always: no secrets in prompts (use env vars), review generated code before running on real data, log tool/agent actions. Golden rule: automate execution, not accountability; treat AI output like a junior colleague's work.

**Best practices (ch. 11).** Be precise on inputs/outputs, give exact formulas, ask for unit tests with code, put conventions in CLAUDE.md, split architecture → validate → implement, read existing code first. Prompt frameworks: ROTA, CRISP, CARE, SMART, COPE. Correction loop: test fails → Claude reads error → fixes → re-runs → you validate. Use synthetic datasets to develop without exposing real data. Quarterly-review pipeline: data-quality assessment (flag, don't fix) → human cleaning decisions applied by script with cleaning log → EDA on clean data → two PDF reports (technical + 2-page exec). Every step saves its script, so reproducibility is the deliverable. Python→R migration: inventory → migrate → reconcile until exact.

**Regulatory references the guide cites (but explicitly does not teach):** IAA ISAP 1/1A, ASOP 56, VM-20/VM-30/VM-G, SR 26-2, OSFI E-23, NAIC AI Model Bulletin, Colorado SB21-169, AMF guideline, DFS Circular Letter 2025-7.

## Caveats worth carrying into agent work

- The guide is a practical starter, not a governance, compliance or software-engineering manual; it says simplifications are used and professional judgment applies.
- Model names in the guide (Haiku/Sonnet/Opus 5.5, Fable 5.1) and UI screenshots will date; the tiering advice (mid-tier for most work, top tier for complex architecture) is the durable part.
- Prompts are starting points; the authors expect iteration. Several flag actuarial/regulatory judgment explicitly (e.g. state restrictions on credit-based insurance scores in use case 24).
- Companion packs are **not** in this repo; they are on Google Drive (see `companion-packs.md`) and must be downloaded manually.

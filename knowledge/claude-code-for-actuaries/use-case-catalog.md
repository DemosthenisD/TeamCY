# Use-case catalog (32 use cases)

Every use case in the guide has: situation, what Claude Code designs, an exhaustive ready-to-paste prompt, expected inputs/outputs. Read the chapter file for the prompt text. `[pack]` = companion pack exists (see `companion-packs.md`).

## Life & Annuities — `chapters/05-life-annuities.txt`

**5.1 ALM team**
1. Valuing a bond portfolio (fixed, floating, inflation-linked, with default/recovery) [pack]
2. Asset-liability projection engine
3. ALM monitoring dashboard
4. Strategic asset allocation

**5.2 Assets and investment strategy**
5. Line-by-line equity projection (performance and dividends)
6. Consolidated multi-class portfolio valuation
7. Investment strategy and allocation rebalancing

**5.3 Modeling team**
8. Developing VBA valuation functions [pack: bond projection, Excel/VBA & Streamlit]
9. Modeling dynamic lapses
10. Stochastic reserves: scenario pipeline and CTE
11. Modeling a GMDB floor guarantee
12. Automatic technical documentation of models

**5.4 Risk measurement and capital**
13. NAIC risk-based capital calculator [pack]
14. Automating ORSA stress tests

**5.5 Model validation and oversight**
15. Validation tool by independent model replication
16. Critical review of a methodology memo

**5.6 Valuation and financial reporting**
17. Statutory reserve calculation at the close
18. Movement analysis and close controls

**5.7 Product development**
19. New product profitability analysis

**5.8 Corporate finance and investments**
20. Performance reporting and attribution

**5.9 Health and group benefits**
21. Health pricing and loss ratio monitoring
22. Disabled-life reserves for disability claims
23. Pandemic experience monitoring, data-visualization storytelling [pack; recommended first project]

## Property & Casualty — `chapters/06-property-casualty.txt`

24. Auto pricing: GLM, machine learning and variable selection [pack: freMTPL2freq]
25. Documentation, backtesting and the rate filing deck [same pack]
26. Reserving: Chain Ladder, Bornhuetter-Ferguson, Mack [2 packs]
27. Profitability analysis and portfolio steering
28. Data visualization and exploratory portfolio analysis
29. Drafting actuarial reports and regulatory watch

## Reinsurance — `chapters/07-reinsurance.txt`

30. Pricing and modeling extreme risks (XL treaty: GPD/lognormal fit, Poisson frequency, Monte Carlo, burning cost, VaR/TVaR)
31. Optimizing the reinsurance program (QS / XL / stop-loss, efficient frontier, capital relief)
32. Ceded reserves and regulatory reporting (Schedule F support, net-to-gross reconciliation)

## Cross-cutting

- Ch. 8 `08-internal-tool-in-a-day.txt`: Streamlit data-quality tool prompt; list of tools buildable in a day.
- Ch. 9 `09-ai-agents.txt`: three agent prompts (spec Q&A, code-vs-spec, data-quality monitoring) [pack].
- Ch. 11 `11-best-practices-workflow.txt`: prompting frameworks, correction loop, synthetic data, quarterly review pipeline [pack], Python→R migration [pack].
- Ch. 12 `12-appendix-claude-md-template.txt`: CLAUDE.md template (also `claude-md-template-actuaries.md`).

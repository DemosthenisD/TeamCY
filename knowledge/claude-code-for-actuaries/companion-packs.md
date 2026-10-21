# Companion project packs (Google Drive)

Each pack = `data/`, `CLAUDE.md`, `PROMPT.md` (ready-to-paste prompt), sometimes reference results. Download each into its own folder, open that folder in Claude Code, trust the workspace, attach PROMPT.md and say "run these instructions please" (guide §3.7). Some datasets keep original French file/column names: leave them unchanged.

| Pack | Guide location | Contents | Link |
|---|---|---|---|
| Bond valuation library | Ch. 5.1, use case 1 | 15-bond synthetic portfolio, zero-coupon and default curves, reference values | https://drive.google.com/drive/folders/1x19EgXttA2kZ3uzicXhrGZ44MUGcvjSt |
| Bond projection, Excel/VBA & Streamlit | Ch. 5.3, use case 8 | Bond table, projected risk-free curves, functional spec, two exercises | https://drive.google.com/drive/folders/1AJquey5o0wMNwjCvaWEFgzUBR22LRt6W |
| NAIC RBC calculator | Ch. 5.4, use case 13 | Exposures and factors workbook, hand-checked reference table | https://drive.google.com/drive/folders/1XLz8xOUH_kJ2ycnd1lki9-v7EDn-2UvA |
| Pandemic data visualization | Ch. 5.9, use case 23 | Three public datasets (hospital, vaccination, economic); recommended first project | https://drive.google.com/drive/folders/19EQDtTzy184cRkDf0piJ3z3yDZFE15FV |
| Auto pricing, GLM vs ML | Ch. 6.1, use cases 24-25 | freMTPL2freq, 678,000 public motor policies (CASdatasets) | https://drive.google.com/drive/folders/1ecttixRLZ8caekAe07FPLjstjcbuA-FR |
| Reserving, Chain Ladder | Ch. 6.2, use case 26 | Ten-year cumulative auto claims triangle, plain Chain Ladder | https://drive.google.com/drive/folders/1de6u09b_EKjSoZ0xWoCk5mNHWvptCmjy |
| Reserving, CL, BF and Mack | Ch. 6.2, use case 26 | Two triangles (auto, homeowners) with premiums and a priori loss ratios, reference results for 3 methods | https://drive.google.com/drive/folders/16LTy7Pv8RMuwg8S6bGyPM317_ugSL5IC |
| AI agent, documentation & code | Ch. 9 | Streamlit + ChromaDB chat app, sample document-and-code corpus | https://drive.google.com/drive/folders/11u0XGYyzjURcAjLFyB9b4X04RtMvZ9U_ |
| Quarterly portfolio review pipeline | Ch. 11 (11.4) | 500,000-policy synthetic portfolio with planted data issues, four chained prompts | https://drive.google.com/drive/folders/1HZClco6imtxk9AFmA8SqVx6uSEUuJDNs |
| Python-to-R migration | Ch. 11 (11.5) | Worked migration of the quarterly-review scripts, reconciliation outputs | https://drive.google.com/drive/folders/1lSVlazcwunVPbD-5UtV2aIcHv-lPTPHE |

All ten in one folder: https://drive.google.com/drive/folders/1A9S1NZ-ueXqX-gmibZPHioXYl07y7Exi

Suggested put-down location on your PC: `knowledge/claude-code-for-actuaries/packs/<pack-name>/` (add `packs/` to `.gitignore` if the data is large).

# Project context
Actuarial model - [Life / P&C / Reinsurance]
Objective: [ALM projection / reserving / pricing / ...]

# Technical stack
- Python 3.11: pandas, numpy, scipy, statsmodels
- Machine learning: scikit-learn, xgboost, shap
- Visualization: matplotlib, plotly, streamlit
- Legacy models in Excel/VBA (folder ./legacy)
- Data: parquet format, monthly time step

# Code conventions
- Variable names and comments in English
- Docstrings for every function (role, inputs, outputs, units)
- Systematic unit tests (pytest) for every calculation function
- Variable naming per the internal actuarial standard

# Business rules
- Always check cash flow consistency before validating
- Discount with the prescribed statutory rates unless told otherwise
- Default mortality: 2017 CSO, age nearest birthday (ANB), gender- and smoker-distinct, select and ultimate
- Every implicit assumption must be documented in the code

# Security and confidentiality
- Never use real personal data: synthetic data only
- Never write secrets in the code
- Flag any code that writes or deletes files before execution

# What I expect from you
- Propose the architecture before implementing large modules
- Write tests at the same time as the code
- Explain modeling choices in plain English
- Flag anything that requires actuarial validation

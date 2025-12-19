# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## Skills to be learnt/tested
- Python
- Virtual environment
- Data management
- Dashboard tools
- Data analysis
- CSS
- Python testing
- Test automation
- Shell scripting

## References
- [Check the Quantium Challenge Yourself!](https://www.theforage.com/simulations/quantium/software-engineering-j6ci)
- [Docs for this project](/quantium-starter-repo/_docs)

## Data processing script
Run the processing script to generate a single cleaned CSV for Pink Morsels sales.

- Command: `python scripts/process_data.py`
- Output: `data/processed/pink_morsels_sales.csv` (columns: Sales, Date, Region)

The script is idempotent and will create the `data/processed/` folder if missing.
# quantium-starter-repo

🎉 **SIMULATION COMPLETED!** Successfully finished Quantium's Software Engineering Job Simulation on Forage.

Pink Morsels sales visualiser built for the Quantium coding challenge. The repository combines ETL data processing with a Dash web application that visualizes sales trends, region-specific performance, and the impact of a price increase event.

## 🏆 Accomplishments
- ✅ Set up a local Python development environment with proper package management and dependencies
- ✅ Implemented robust ETL pipeline to clean and normalize multiple CSV sources into a single source-of-truth dataset
- ✅ Built an interactive Dash application with region filtering and time-series visualization using Plotly
- ✅ Designed an intuitive UI with custom CSS styling and responsive layout for improved user experience
- ✅ Created comprehensive pytest test suite to validate app components and ensure reliability
- ✅ Automated test execution with shell script and CI/CD integration via GitHub Actions
- 🔗 [View the simulation](https://www.theforage.com/simulations/quantium/software-engineering-j6ci)

## Overview
- **Role**: Software engineer building data visualization tools for Soul Foods' retail analytics team
- **Goal**: Process sales data and create an interactive dashboard to analyze Pink Morsels product performance before/after a price increase
- **Stack**: Dash (Plotly), pandas for data processing, pytest for testing, GitHub Actions for CI

## What's in this repo
- Task instructions and guidance in [`_docs/`](./_docs). Each task folder (task1–task6) contains descriptions and requirements
- Raw sales data at [`data/daily_sales_data_*.csv`](./data), ETL output at [`data/processed/pink_morsels_sales.csv`](./data/processed/pink_morsels_sales.csv)
- Dash application in [`pink_morsels/`](./pink_morsels) package with modular architecture:
  - [`pink_morsels/data.py`](./pink_morsels/data.py) — data loading and region aggregation
  - [`pink_morsels/viz.py`](./pink_morsels/viz.py) — Plotly figure construction
  - [`pink_morsels/web.py`](./pink_morsels/web.py) — Dash layout and callbacks
- Tests in [`tests/test_app.py`](./tests/test_app.py)
- Automation: [`scripts/run_tests.sh`](./scripts/run_tests.sh) and [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

## Run the Dash app
1. **Prerequisites**: Python 3.8+ and pip
2. **Install dependencies and launch**:

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# (Optional) Regenerate processed data
python scripts/process_data.py

# Run the app
python app.py
```

Open http://127.0.0.1:8050 in your browser.

## Run tests
Install the project in editable mode, then run pytest:

```bash
pip install -e .
pytest -q
```

Or use the automated test runner (creates/activates venv, installs deps, runs tests):

```bash
bash scripts/run_tests.sh
```

## App capabilities
- **Entry point** [`app.py`](./app.py): launches the Dash server using `create_app()` from the package
- **Data layer** [`pink_morsels/data.py`](./pink_morsels/data.py): loads CSV, aggregates by date/region, handles missing values
- **Visualization** [`pink_morsels/viz.py`](./pink_morsels/viz.py): creates time-series line chart with price-increase annotation
- **UI/callbacks** [`pink_morsels/web.py`](./pink_morsels/web.py): region picker radio buttons, graph component, callback for filtering
- **Styling** [`assets/style.css`](./assets/style.css): custom CSS for clean, modern look

## Quick orientation
- Follow the task guides in [`_docs/`](./_docs) to understand the challenge requirements and deliverables
- Use [`scripts/process_data.py`](./scripts/process_data.py) to regenerate the processed CSV from raw data
- The architecture is modular: data, viz, and web concerns are separated for maintainability and testing
- CI workflow automatically runs tests on every push/PR to ensure code quality

---

## 🎄 Celebration

Happy holidays! Here's a festive ASCII tree to mark the special day:

```
        *
       /|\
      /*|O\
     /*/|\*\
    /X/\|/*\X\
   /X/*/X\*\X\
  /*/\X/\*\X/\
 /X/O/\*\O/\X\
/*/\X/\*\X/\*\
      |||
     /___\
```

**Made with ❤️ + ☕ on Christmas Day 2025** 🎅
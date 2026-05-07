# Python Coding Interview Challenge: Campaign Data Analysis

## Context

You have been provided with a Python script (`analyze_campaigns.py`) and a data file (`campaign_data.csv`) containing marketing transactions. The script is incomplete and contains several bugs. The data itself is messy and reflects real-world quality issues.

## Your Task (30 minutes)

Your objective is to debug and complete the `analyze_campaigns.py` script to meet the following requirement:

**Requirement:** The script must process `campaign_data.csv` and generate a new file named `campaign_summary.csv`. This summary file must contain the following columns:
- `campaign_name`
- `total_revenue` (the total revenue from 'completed' transactions)
- `unique_completed_transactions` (the count of unique 'completed' transactions)

## Setup

**Requirements:** Python 3.8+

1. Clone this repository:
   ```bash
   git clone git@github.com:Danielmtv1/challenge_python-sql.git
   cd challenge_python-sql
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   # venv\Scripts\activate         # Windows
   ```

3. Install dependencies:
   ```bash
   pip install pandas
   ```

4. Run the script to see the initial state:
   ```bash
   python analyze_campaigns.py
   ```

## Instructions

1.  Review the `analyze_campaigns.py` script and the `campaign_data.csv` file.
2.  Modify the script to fix all bugs and implement the required logic. Follow the `# TODO` comments as a guide.
3.  Ensure your final script runs without errors and produces the correct `campaign_summary.csv` file.

## Tip

The script is designed to fail if you run it immediately. Before writing too much code, we highly recommend you **explore the Pandas DataFrame** after loading it (e.g., using `df.info()`, `df.head()`) to diagnose the data quality issues.

Good luck!

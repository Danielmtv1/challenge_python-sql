# Python Coding Interview Challenge: Campaign Data Analysis

## Context

You have been provided with a Python script (`analyze_campaigns.py`) and a data file (`campaign_data.csv`) containing marketing transactions. The script is incomplete and contains several bugs. The data itself is messy and reflects real-world quality issues.

## Your Task (30 minutes)

Your objective is to debug and complete the `analyze_campaigns.py` script to meet the following requirement:

**Requirement:** The script must process `campaign_data.csv` and generate a new file named `campaign_summary.csv`. This summary file must contain the following columns:
- `campaign_name`
- `total_revenue` (the total revenue from 'completed' transactions)
- `unique_completed_transactions` (the count of unique 'completed' transactions)

## Instructions

1.  Clone this repository to your local machine.
2.  Review the `analyze_campaigns.py` script and the `campaign_data.csv` file.
3.  Modify the script to fix all bugs and implement the required logic. Follow the `# TODO` comments as a guide.
4.  Ensure your final script runs without errors and produces the correct `campaign_summary.csv` file.

## Tip

The script is designed to fail if you run it immediately. Before writing too much code, we highly recommend you **explore the Pandas DataFrame** after loading it (e.g., using `df.info()`, `df.head()`) to diagnose the data quality issues.

Good luck!

import pandas as pd

def process_campaign_data(filepath):
    print("Loading data...")
    df = pd.read_csv(filepath)

    print("\nInitial data shape:", df.shape)
    print(df.head())

    print("\n--- Starting Data Processing ---")

    # TODO (a): Fix transaction_amount conversion
    # The 'transaction_amount' column contains text (currency symbols, commas, empty strings).
    # Clean it and convert the column to float.
    # (If you run this script right now, it will fail here or silently ignore the calculation later).

    # df['transaction_amount'] = ???


    # TODO (b): Standardize the 'status' column
    # Values are inconsistent ('Completed', 'completed', 'COMPLETED'). Standardize them.

    # df['status'] = ???


    # TODO (c): Convert dates
    # Convert 'transaction_date' from strings to proper datetime objects.
    # Note: the column contains mixed date formats.

    # df['transaction_date'] = ???


    # TODO (d): Handle duplicates
    # There are fully duplicated rows in the dataset. Remove them.

    # df = ???


    print("\n--- Starting Analysis ---")

    # TODO (e): Filter data
    # We only want to analyze successful transactions.
    # FIX THE BUG: If you didn't standardize the status properly in step (b),
    # this filter will silently drop valid rows.
    completed_df = df[df['status'] == 'completed']

    print(f"Transactions after filter: {len(completed_df)}")


    # TODO (f): Calculate total revenue per campaign
    # FIX THE BUG: This current aggregation is summing ALL numeric columns (like transaction_id).
    # We only want the sum of the transaction_amount.
    campaign_revenue = completed_df.groupby('campaign_name').sum()


    # TODO (g): Calculate unique transactions
    # Count the number of UNIQUE transaction_ids per campaign.

    # campaign_transaction_count = ???


    # TODO (h): Final Export
    # Combine the revenue and unique transaction count into a single final DataFrame.
    # Export the final result to 'campaign_summary.csv'

    # final_summary_df.to_csv('campaign_summary.csv', index=True)

    print("\nProcess finished. Please check your CSV output.")

if __name__ == "__main__":
    process_campaign_data('campaign_data.csv')

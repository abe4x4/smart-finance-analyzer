from collections import defaultdict
import os
from datetime import datetime

# -----------------------------------------------------
# ANALYZE: Financial Summary
# -----------------------------------------------------
def analyze_finances(transactions):
    """
    Calculates and displays total credits, debits, transfers, and net balance.
    Also shows grouped totals by type.
    
    Parameters:
    - transactions (list): A list of transaction dictionaries.
    
    Each transaction must contain:
      - 'type': 'credit', 'debit', or 'transfer'
      - 'amount': float (debits are stored as negative)
    """
    print("\n--- Financial Summary ---")

    # Initialize a dictionary to hold totals by transaction type
    totals = defaultdict(float)

    # Loop through transactions and sum by type
    for t in transactions:
        t_type = t['type']
        totals[t_type] += t['amount']  # debit is already negative

    # Extract and format values for display
    total_credit = totals['credit']
    total_debit = abs(totals['debit'])  # show as positive
    total_transfer = totals['transfer']
    net_balance = total_credit - total_debit

    # Display main summary
    print(f"Total Credits:   ${total_credit:,.2f}")
    print(f"Total Debits:    ${total_debit:,.2f}")
    print(f"Total Transfers: ${total_transfer:,.2f}")
    print(f"Net Balance:     ${net_balance:,.2f}")

    # Show totals by transaction type
    print("\nBy Type:")
    for t_type, amount in totals.items():
        print(f"  {t_type.title():<10}: ${abs(amount):,.2f}")

# -----------------------------------------------------
# GENERATE REPORT: Save Summary to File
# -----------------------------------------------------
def generate_report(transactions, output_dir='reports'):
    """
    Generate a financial summary report and save it as a text file with a timestamp.
    Includes totals, net balance, and the date range of transactions.
    
    Parameters:
    - transactions (list): List of transaction dictionaries
    - output_dir (str): Folder to save the report file
    """
    if not transactions:
        print("⚠️ No transactions to generate a report.")
        return

    # Step 1: Calculate totals
    totals = defaultdict(float)
    for t in transactions:
        totals[t['type']] += t['amount']  # debit remains negative

    net_balance = totals['credit'] - abs(totals['debit'])

    # Step 2: Get date range
    dates = [t['date'] for t in transactions]
    start_date = min(dates).strftime('%Y-%m-%d')
    end_date = max(dates).strftime('%Y-%m-%d')

    # Step 3: Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Step 4: Create timestamped filename
    today_str = datetime.today().strftime('%Y%m%d')
    filename = os.path.join(output_dir, f"report_{today_str}.txt")

    # Step 5: Write the report to file
    try:
        with open(filename, 'w') as f:
            f.write("Smart Personal Finance Analyzer Report\n")
            f.write(f"Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Date Range: {start_date} to {end_date}\n\n")
            f.write(f"Total Credits   : ${totals['credit']:.2f}\n")
            f.write(f"Total Debits    : ${abs(totals['debit']):.2f}\n")
            f.write(f"Total Transfers : ${totals['transfer']:.2f}\n")
            f.write(f"Net Balance     : ${net_balance:.2f}\n\n")
            f.write("By Type:\n")
            for ttype, amount in totals.items():
                f.write(f"  {ttype.capitalize():<10}: ${abs(amount):.2f}\n")

        print(f"📄 Report successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving report: {e}")

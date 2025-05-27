from collections import defaultdict

# -----------------------------------------------------
# ANALYZE: Financial Summary
# -----------------------------------------------------
def analyze_finances(transactions):
    """
    Calculates and displays total credits, debits, transfers, and net balance.
    Also shows grouped totals by type.

    Parameters:
    transactions (list): A list of dictionaries where each dictionary represents a transaction.
    
    Each transaction must contain:
        - 'type': 'credit', 'debit', or 'transfer'
        - 'amount': numeric value (float)
    
    Debits are recorded as negative numbers, so we use abs() to show them as positive.
    """
    print("\n--- Financial Summary ---")

    # Create a dictionary to accumulate totals for each transaction type
    totals = defaultdict(float)

    # Loop through all transactions to categorize and sum amounts by type
    for t in transactions:
        t_type = t['type']  # e.g., 'credit', 'debit', 'transfer'
        totals[t_type] += t['amount']

    # Assign totals to variables (convert debit to positive for display)
    total_credit = totals['credit']
    total_debit = abs(totals['debit'])
    total_transfer = totals['transfer']
    net_balance = total_credit - total_debit

    # Display summary results
    print(f"Total Credits:   ${total_credit:,.2f}")
    print(f"Total Debits:    ${total_debit:,.2f}")
    print(f"Total Transfers: ${total_transfer:,.2f}")
    print(f"Net Balance:     ${net_balance:,.2f}")

    # Display breakdown by type
    print("\nBy Type:")
    for t_type, amount in totals.items():
        print(f"  {t_type.title():<10}: ${abs(amount):,.2f}")

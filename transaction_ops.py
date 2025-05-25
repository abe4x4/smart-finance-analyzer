# transaction_ops.py
from datetime import datetime

# -----------------------------------------------------
# ADD a new transaction to the list
# -----------------------------------------------------
def add_transaction(transactions):
    """
    Prompts the user for new transaction details,
    validates inputs, and adds the transaction to the list.
    """
    print("\n--- Add New Transaction ---")

    try:
        # Step 1: Generate a new transaction ID (max ID + 1)
        transaction_id = max([t['transaction_id'] for t in transactions], default=0) + 1

        # Step 2: Prompt for and parse date
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Step 3: Customer ID
        customer_id = int(input("Enter customer ID: "))

        # Step 4: Amount (must be positive, will be flipped if debit)
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("⚠️ Amount should be positive. We'll adjust it if it's a debit.")
            amount = abs(amount)

        # Step 5: Type (credit, debit, or transfer)
        trans_type = input("Enter type (credit/debit/transfer): ").strip().lower()
        if trans_type not in ['credit', 'debit', 'transfer']:
            print("❌ Invalid transaction type.")
            return
        if trans_type == 'debit':
            amount = -amount  # Convert debit to negative value

        # Step 6: Description
        description = input("Enter description: ").strip()

        # Step 7: Create the dictionary
        transaction = {
            'transaction_id': transaction_id,
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': trans_type,
            'description': description
        }

        # Step 8: Add to the list
        transactions.append(transaction)
        print("✅ Transaction added successfully!")

    except ValueError as e:
        print(f"❌ Input error: {e}")


# -----------------------------------------------------
# VIEW all transactions in a readable format
# -----------------------------------------------------
def view_transactions(transactions):
    """
    Display all transactions in a neat table layout with column alignment.
    """
    if not transactions:
        print("\nNo transactions to display.")
        return

    print("\n--- All Transactions ---")

    # Define column headers and their widths
    headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
    print("{:<5} {:<12} {:<10} {:>10} {:<10} {}".format(*headers))
    print("-" * 70)

    for t in transactions:
        print("{:<5} {:<12} {:<10} {:>10.2f} {:<10} {}".format(
            t['transaction_id'],
            t['date'].strftime('%Y-%m-%d'),
            t['customer_id'],
            t['amount'],
            t['type'],
            t['description']
        ))

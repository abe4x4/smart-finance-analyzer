from datetime import datetime
from utils.finance_utils import load_transactions

# -----------------------------------------------------
# ADD a new transaction to the list
# -----------------------------------------------------
def add_transaction(transactions):
    print("\n--- Add New Transaction ---")
    try:
        # Automatically determine the next transaction ID
        transaction_id = max([t['transaction_id'] for t in transactions], default=0) + 1

        # Get and validate date
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Get customer ID and amount
        customer_id = int(input("Enter customer ID: "))
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("⚠️ Amount should be positive. We'll adjust it if it's a debit.")
            amount = abs(amount)

        # Validate transaction type
        trans_type = input("Enter type (credit/debit/transfer): ").strip().lower()
        if trans_type not in ['credit', 'debit', 'transfer']:
            print("❌ Invalid transaction type.")
            return

        # Convert debit to negative amount
        if trans_type == 'debit':
            amount = -amount

        # Get description
        description = input("Enter description: ").strip()

        # Create the transaction dictionary
        transaction = {
            'transaction_id': transaction_id,
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': trans_type,
            'description': description
        }

        # Add transaction to the list
        transactions.append(transaction)
        print("✅ Transaction added successfully!")

    except ValueError as e:
        print(f"❌ Input error: {e}")

# -----------------------------------------------------
# VIEW all transactions in a readable format
# -----------------------------------------------------
def view_transactions(transactions):
    if not transactions:
        print("\nNo transactions to display.")
        return

    print("\n--- All Transactions ---")
    headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
    print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(*headers))
    print("-" * 75)

    for t in transactions:
        # Format amount with parentheses for debits
        amount_str = f"({abs(t['amount']):.2f})" if t['type'] == 'debit' else f"{t['amount']:.2f}"
        print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(
            t['transaction_id'],
            t['date'].strftime('%Y-%m-%d'),
            t['customer_id'],
            amount_str,
            t['type'],
            t['description']
        ))

# -----------------------------------------------------
# VIEW transactions directly from the file
# -----------------------------------------------------
def view_transactions_from_file():
    try:
        # Load transactions from file
        file_transactions = load_transactions()

        if not file_transactions:
            print("\nThe transaction file is empty or invalid.")
            return

        print("\n--- Transactions from File ---")
        headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
        print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(*headers))
        print("-" * 75)

        for t in file_transactions:
            # Format amount with parentheses for debits
            amount_str = f"({abs(t['amount']):.2f})" if t['type'] == 'debit' else f"{t['amount']:.2f}"
            print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(
                t['transaction_id'],
                t['date'].strftime('%Y-%m-%d'),
                t['customer_id'],
                amount_str,
                t['type'],
                t['description']
            ))

    except Exception as e:
        print(f"❌ Failed to load or display transactions from file: {e}")

# -----------------------------------------------------
# UPDATE an existing transaction
# -----------------------------------------------------
def update_transaction(transactions):
    try:
        transaction_id = int(input("\nEnter the transaction ID to update: "))
        for t in transactions:
            if t['transaction_id'] == transaction_id:
                print("Leave any field blank to keep the current value.")

                # Prompt for new values and update only if input is not blank
                new_date = input(f"Date ({t['date'].strftime('%Y-%m-%d')}): ").strip()
                if new_date:
                    t['date'] = datetime.strptime(new_date, "%Y-%m-%d")
                new_cust_id = input(f"Customer ID ({t['customer_id']}): ").strip()
                if new_cust_id:
                    t['customer_id'] = int(new_cust_id)
                new_amount = input(f"Amount ({t['amount']}): ").strip()
                if new_amount:
                    t['amount'] = float(new_amount)
                new_type = input(f"Type ({t['type']}): ").strip().lower()
                if new_type:
                    if new_type not in ['credit', 'debit', 'transfer']:
                        print("❌ Invalid type. Update canceled.")
                        return
                    t['type'] = new_type
                new_desc = input(f"Description ({t['description']}): ").strip()
                if new_desc:
                    t['description'] = new_desc

                print("✅ Transaction updated successfully!")
                return

        print("❌ Transaction ID not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

# -----------------------------------------------------
# DELETE a transaction by ID
# -----------------------------------------------------
def delete_transaction(transactions):
    try:
        transaction_id = int(input("\nEnter the transaction ID to delete: "))
        for index, t in enumerate(transactions):
            if t['transaction_id'] == transaction_id:
                # Show transaction details before confirmation
                print("Transaction details:")
                print(f"{t['transaction_id']} | {t['date'].strftime('%Y-%m-%d')} | {t['customer_id']} | {t['amount']} | {t['type']} | {t['description']}")
                confirm = input("Are you sure you want to delete this transaction? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    del transactions[index]
                    print("🗑️ Transaction deleted.")
                    return
                else:
                    print("❌ Deletion canceled.")
                    return

        print("❌ Transaction ID not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

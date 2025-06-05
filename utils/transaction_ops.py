from datetime import datetime
from utils.analysis import load_transactions


# -----------------------------------------------------
# ADD a new transaction to the list (with auto defaults)
# -----------------------------------------------------
def add_transaction(transactions):
    """
    Prompt the user to input transaction details and add it to the transactions list.
    Provides sensible defaults if user presses Enter:
      - Automatically uses the next transaction ID
      - Uses today's date if no date provided
      - Uses next customer ID if not provided
      - Accepts 'c', 'd', 't' for credit, debit, transfer
    """
    print("\n--- Add New Transaction ---")
    try:
        # Determine the next transaction ID
        transaction_id = max([t['transaction_id'] for t in transactions], default=0) + 1
        print(f"ℹ️ Using next transaction ID: {transaction_id}")

        # Prompt for date with default to today
        date_str = input("Enter date (YYYY-MM-DD) [Press Enter for today]: ").strip()
        if not date_str:
            date = datetime.today()
            print(f"📅 Using today's date: {date.strftime('%Y-%m-%d')}")
        else:
            date = datetime.strptime(date_str, "%Y-%m-%d")

        # Prompt for customer ID with default to next available
        customer_ids = [t['customer_id'] for t in transactions]
        next_customer_id = max(customer_ids, default=0) + 1
        cust_input = input(f"Enter customer ID [Press Enter for next ID: {next_customer_id}]: ").strip()
        if not cust_input:
            customer_id = next_customer_id
            print(f"👤 Using next customer ID: {customer_id}")
        else:
            customer_id = int(cust_input)

        # Prompt for amount and validate it
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("⚠️ Amount should be positive. It will be adjusted if it's a debit.")
            amount = abs(amount)

        # Prompt for transaction type with shorthand
        print("Enter type: [c=credit, d=debit, t=transfer]")
        type_input = input("Type: ").strip().lower()
        type_map = {'c': 'credit', 'd': 'debit', 't': 'transfer'}
        if type_input not in type_map:
            print("❌ Invalid type. Must be c, d, or t.")
            return
        trans_type = type_map[type_input]

        # Convert debit to negative amount
        if trans_type == 'debit':
            amount = -amount

        # Prompt for description
        description = input("Enter description: ").strip()

        # Create transaction dictionary
        transaction = {
            'transaction_id': transaction_id,
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': trans_type,
            'description': description
        }

        # Add to list
        transactions.append(transaction)
        print("✅ Transaction added successfully!")

    except ValueError as e:
        print(f"❌ Input error: {e}")

# -----------------------------------------------------
# VIEW all in-memory transactions in table format
# -----------------------------------------------------
def view_transactions(transactions):
    """
    Display all transactions currently held in memory.
    """
    if not transactions:
        print("\nNo transactions to display.")
        return

    print("\n--- All Transactions ---\n")
    # Print header
    headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
    print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(*headers))
    print("-" * 75)

    for t in transactions:
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
# VIEW transactions from the CSV file
# -----------------------------------------------------
def view_transactions_from_file():
    """
    Load and display transactions directly from the saved CSV file.
    """
    try:
        file_transactions = load_transactions()

        if not file_transactions:
            print("\nThe transaction file is empty or invalid.")
            return

        print("\n--- Transactions from File ---")
        headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
        print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(*headers))
        print("-" * 75)

        for t in file_transactions:
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
# UPDATE a specific transaction by ID
# -----------------------------------------------------
def update_transaction(transactions):
    """
    Allow the user to update fields of an existing transaction by ID.
    """
    try:
        transaction_id = int(input("\nEnter the transaction ID to update: "))
        for t in transactions:
            if t['transaction_id'] == transaction_id:
                print("Leave any field blank to keep the current value.")

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

                print("\n✅ Transaction updated successfully!")
                return

        print("❌ Transaction ID not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

# -----------------------------------------------------
# DELETE a transaction by ID
# -----------------------------------------------------
def delete_transaction(transactions):
    """
    Prompt the user to delete a transaction by ID, with confirmation.
    Accepts 'y' or 'yes' to confirm, 'n' or 'no' to cancel.
    Repeats prompt until valid input is received.
    """
    try:
        transaction_id = int(input("\nEnter the transaction ID to delete: "))
        for index, t in enumerate(transactions):
            if t['transaction_id'] == transaction_id:
                print("Transaction details:")
                print(f"{t['transaction_id']} | {t['date'].strftime('%Y-%m-%d')} | {t['customer_id']} | {t['amount']} | {t['type']} | {t['description']}")

                # Ask for confirmation until a valid input is received
                while True:
                    confirm = input("Are you sure you want to delete this transaction? (y/yes or n/no): ").strip().lower()

                    if confirm in ['yes', 'y']:
                        del transactions[index]
                        print("🗑️ Transaction deleted.")
                        return
                    elif confirm in ['no', 'n']:
                        print("❌ Deletion canceled.")
                        return
                    else:
                        print("⚠️ Invalid input. Please enter 'y'/'yes' or 'n'/'no'.")
                
        print("❌ Transaction ID not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

# -----------------------------------------------------
# Filter Transactions by Year
# -----------------------------------------------------
def filter_transactions_by_year(transactions):
    """
    Prompt the user to enter a year and filter transactions for that year.
    Display the filtered transactions in a table format.
    """
    if not transactions:
        print("⚠️ No transactions available to filter.")
        return

    try:
        year_input = input("Enter the year to filter by (e.g. 2024): ").strip()
        if not year_input.isdigit():
            print("❌ Invalid year format.")
            return

        year = int(year_input)
        filtered = [t for t in transactions if t['date'].year == year]

        if not filtered:
            print(f"📭 No transactions found for the year {year}.")
            return

        print(f"\n--- Transactions for {year} ---")
        headers = ['ID', 'Date', 'Customer', 'Amount', 'Type', 'Description']
        print("{:<5} {:<12} {:<10} {:>12} {:<10} {}".format(*headers))
        print("-" * 75)

        for t in filtered:
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
        print(f"❌ Error filtering by year: {e}")

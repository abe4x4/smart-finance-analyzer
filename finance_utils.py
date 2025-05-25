import csv
from datetime import datetime

# -----------------------------------------------------
# Helper Function: Log error messages to a file
# -----------------------------------------------------
def log_error(message):
    """
    Logs an error message into 'errors.txt'.
    If the file doesn't exist, it will be created.
    'a' mode appends to the file so previous logs are preserved.
    """
    with open("errors.txt", "a") as f:
        f.write(message + "\n")  # Write the error followed by a new line


# -----------------------------------------------------
# Load Transactions from the CSV File
# -----------------------------------------------------
def load_transactions(filename="data/financial_transactions.csv"):
    """
    Loads valid transactions from a CSV file into a list of dictionaries.
    Invalid rows (e.g. bad date format or missing fields) are skipped.
    Each valid transaction is returned as a structured dictionary.
    """
    transactions = []  # This list will store the validated transaction records

    try:
        # Open the CSV file using 'with' to ensure it closes automatically
        with open(filename, "r") as file:
            reader = csv.DictReader(file)  # Read each row as a dictionary

            for row in reader:
                try:
                    # Convert and clean fields from string to correct data types
                    transaction_id = int(row['transaction_id'])
                    date = datetime.strptime(row['date'], '%Y-%m-%d')  # Convert date string to datetime
                    customer_id = int(row['customer_id'])
                    amount = float(row['amount'])
                    trans_type = row['type'].strip().lower()
                    description = row['description'].strip()

                    # Validate transaction type
                    if trans_type not in ['credit', 'debit', 'transfer']:
                        raise ValueError(f"Invalid transaction type: {trans_type}")

                    # Convert debits to negative values
                    if trans_type == 'debit':
                        amount = -abs(amount)

                    # Store the transaction as a dictionary
                    transaction = {
                        'transaction_id': transaction_id,
                        'date': date,
                        'customer_id': customer_id,
                        'amount': amount,
                        'type': trans_type,
                        'description': description
                    }

                    transactions.append(transaction)  # Add to list of valid transactions

                except ValueError as ve:
                    # Log the error for this row and skip it
                    print(f"⚠️ Skipping invalid row: {ve}")
                    log_error(f"Row skipped: {row} -> {ve}")

    except FileNotFoundError:
        # If the CSV file is not found, log and report the error
        print("❌ Error: CSV file not found.")
        log_error("FileNotFoundError: Could not open financial_transactions.csv")

    print(f"✅ {len(transactions)} transactions loaded.")
    return transactions


# -----------------------------------------------------
# Save Transactions to the CSV File
# -----------------------------------------------------
def save_transactions(transactions, filename="data/financial_transactions.csv"):
    """
    Saves all transactions to a CSV file.
    It overwrites the current file to keep only the latest records.
    Dates are converted back to string format for saving.
    """
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ['transaction_id', 'date', 'customer_id', 'amount', 'type', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write column headers

            for t in transactions:
                writer.writerow({
                    'transaction_id': t['transaction_id'],
                    'date': t['date'].strftime('%Y-%m-%d'),  # convert date back to string
                    'customer_id': t['customer_id'],
                    'amount': t['amount'],
                    'type': t['type'],
                    'description': t['description']
                })

        print("💾 Transactions saved successfully.")

    except Exception as e:
        print(f"❌ Failed to save transactions: {e}")
        log_error(f"Save error: {e}")


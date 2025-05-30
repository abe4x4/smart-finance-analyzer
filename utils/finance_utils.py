from datetime import datetime
import os
import shutil
import csv

# -----------------------------------------------------
# LOAD transactions from CSV
# -----------------------------------------------------
def load_transactions(filename='data/financial_transactions.csv'):
    """
    Load transactions from a CSV file.
    Returns a list of transaction dictionaries.
    Skips rows with invalid data and logs errors.
    """
    transactions = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    date = datetime.strptime(row['date'], '%Y-%m-%d')
                    amount = float(row['amount'])
                    if row['type'] == 'debit':
                        amount = -abs(amount)  # Ensure it's negative
                    transaction = {
                        'transaction_id': int(row['transaction_id']),
                        'date': date,
                        'customer_id': int(row['customer_id']),
                        'amount': amount,
                        'type': row['type'],
                        'description': row['description']
                    }
                    transactions.append(transaction)
                except Exception as e:
                    with open("errors.txt", "a") as err_file:
                        err_file.write(f"Skipping row due to error: {e}\n")
        print(f"✅ {len(transactions)} transactions successfully loaded from {filename}")
        return transactions

    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return []

    except Exception as e:
        print(f"❌ Error loading transactions: {e}")
        return []

# -----------------------------------------------------
# SAVE transactions to CSV and BACKUP original if not yet saved
# -----------------------------------------------------
def save_transactions(transactions, filename='data/financial_transactions.csv'):
    """
    Save a list of transactions to a CSV file.
    If a backup doesn't exist, create one first in the backup folder.
    """
    backup_path = 'data/backup/financial_transactions_original.csv'

    # If no backup exists, create it before overwriting the CSV
    if not os.path.exists(backup_path):
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        if os.path.exists(filename):
            shutil.copy(filename, backup_path)
            print(f"📦 Original CSV backed up to {backup_path}")
        else:
            print("⚠️ Warning: No original file found to backup.")

    # Now write the transactions to the CSV
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['transaction_id', 'date', 'customer_id', 'amount', 'type', 'description'])
            writer.writeheader()
            for t in transactions:
                writer.writerow({
                    'transaction_id': t['transaction_id'],
                    'date': t['date'].strftime('%Y-%m-%d'),
                    'customer_id': t['customer_id'],
                    'amount': t['amount'],
                    'type': t['type'],
                    'description': t['description']
                })
        print(f"💾 Transactions saved to {filename}")

    except Exception as e:
        print(f"❌ Error saving transactions: {e}")

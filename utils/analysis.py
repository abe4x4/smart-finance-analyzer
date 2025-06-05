from datetime import datetime
import os
import shutil
import csv
from collections import defaultdict

# -----------------------------------------------------
# HELPER FUNCTION: Parse a single transaction row
# -----------------------------------------------------
def parse_transaction_row(row):
    """
    Validate and convert a CSV row into a transaction dictionary.
    Returns a valid transaction dictionary or raises ValueError.

    Expected CSV fields:
      - transaction_id: int
      - date: string in YYYY-MM-DD format
      - customer_id: int
      - amount: float
      - type: 'credit', 'debit', or 'transfer'
      - description: string
    """
    try:
        transaction = {
            'transaction_id': int(row['transaction_id']),
            'date': datetime.strptime(row['date'], '%Y-%m-%d'),
            'customer_id': int(row['customer_id']),
            'amount': float(row['amount']),
            'type': row['type'].strip().lower(),
            'description': row['description'].strip()
        }

        if transaction['type'] not in ['credit', 'debit', 'transfer']:
            raise ValueError(f"Invalid transaction type: {transaction['type']}")

        if transaction['type'] == 'debit':
            transaction['amount'] = -abs(transaction['amount'])

        return transaction

    except Exception as e:
        raise ValueError(f"Row parsing error: {e}")

# -----------------------------------------------------
# Option 1. LOAD transactions from CSV file
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
                    transaction = parse_transaction_row(row)
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
# Option 7. SAVE transactions to CSV and BACKUP original if not yet saved
# -----------------------------------------------------
def save_transactions(transactions, filename='data/financial_transactions.csv'):
    """
    Save a list of transactions to a CSV file.
    If a backup of the original file doesn't exist, create it first in the backup folder.
    """
    backup_path = 'data/backup/financial_transactions_original.csv'

    # If backup file doesn't exist, create it
    if not os.path.exists(backup_path):
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        if os.path.exists(filename):
            shutil.copy(filename, backup_path)
            print(f"📦 Original CSV backed up to {backup_path}")
        else:
            print("⚠️ Warning: No original file found to backup.")

    # Write current transactions to CSV
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

# -----------------------------------------------------
# Option 6. ANALYZE: Financial Summary
# -----------------------------------------------------
def analyze_finances(transactions):
    """
    Calculates and displays total credits, debits, transfers, and net balance.
    """
    print("\n--- Financial Summary ---\n")
    totals = defaultdict(float)

    for t in transactions:
        t_type = t['type']
        totals[t_type] += t['amount']

    total_credit = totals['credit']
    total_debit = abs(totals['debit'])  # Show as positive
    total_transfer = totals['transfer']
    net_balance = total_credit - total_debit

    print(f"Total Credits   : ${total_credit:,.2f}")
    print(f"Total Debits    : ${total_debit:,.2f}")
    print(f"Total Transfers : ${total_transfer:,.2f}")
    print(f"Net Balance     : ${net_balance:,.2f}")


# -----------------------------------------------------
# Option 8. GENERATE: Summary Report to Text File
# -----------------------------------------------------
def generate_report(transactions, output_dir='reports'):
    """
    Generate a financial summary report and save it as a text file with a timestamp.
    The report includes totals by type and net balance.
    """
    if not transactions:
        print("⚠️ No transactions to generate a report.")
        return

    totals = {'credit': 0, 'debit': 0, 'transfer': 0}
    for t in transactions:
        totals[t['type']] += abs(t['amount'])
    net_balance = totals['credit'] - totals['debit']

    dates = [t['date'] for t in transactions]
    start_date = min(dates).strftime('%Y-%m-%d')
    end_date = max(dates).strftime('%Y-%m-%d')

    os.makedirs(output_dir, exist_ok=True)
    today_str = datetime.today().strftime('%Y%m%d')
    filename = os.path.join(output_dir, f"report_{today_str}.txt")

    try:
        with open(filename, 'w') as f:
            f.write("Smart Personal Finance Analyzer Report\n")
            f.write(f"Generated on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Date Range: {start_date} to {end_date}\n\n")
            f.write(f"Total Credits   : ${totals['credit']:.2f}\n")
            f.write(f"Total Debits    : ${totals['debit']:.2f}\n")
            f.write(f"Total Transfers : ${totals['transfer']:.2f}\n")
            f.write(f"Net Balance     : ${net_balance:.2f}\n")
            f.write("\nBy Type:\n")
            for ttype, amount in totals.items():
                f.write(f"  {ttype.capitalize():<10}: ${amount:.2f}\n")

        print(f"📄 Report successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving report: {e}")

# -----------------------------------------------------
# MONTHLY SUMMARY: Step 8 & 9
# -----------------------------------------------------
def calculate_monthly_summary(transactions):
    """
    Calculates and prints total income (credits), expenses (debits),
    and net balance per month.
    """
    if not transactions:
        print("⚠️ No transactions available to summarize.")
        return

    print("\n--- Monthly Summary ---")
    summary = defaultdict(lambda: {'credit': 0.0, 'debit': 0.0})
    for t in transactions:
        month_key = t['date'].strftime('%Y-%m')
        if t['type'] == 'credit':
            summary[month_key]['credit'] += t['amount']
        elif t['type'] == 'debit':
            summary[month_key]['debit'] += abs(t['amount'])

    for month in sorted(summary.keys()):
        credit = summary[month]['credit']
        debit = summary[month]['debit']
        net = credit - debit
        print(f"{month} => Income: ${credit:.2f}, Expenses: ${debit:.2f}, Net: ${net:.2f}")

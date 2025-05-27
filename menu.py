# menu.py
from finance_utils import load_transactions, save_transactions
from transaction_ops import (
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    view_transactions_from_file
)
from analysis import analyze_finances


# from analysis import analyze_finances, generate_report, calculate_monthly_summary

# Global list to store the transactions in memory
transactions = []

def show_menu():
    """
    Display a text-based CLI menu and route the user's input to appropriate functions.
    The menu loops until the user chooses to exit.
    """
    global transactions

    while True:
        print("\n====== Smart Personal Finance Analyzer ======")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Monthly Summary (Income, Expenses, Balance)")
        print("10. View Transactions from File")
        print("11. Exit")
        print("==============================================")

        choice = input("\nEnter your choice (1–11): ").strip()

        if choice == "1":
            transactions = load_transactions()

        elif choice == "2":
            add_transaction(transactions)

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            update_transaction(transactions)

        elif choice == "5":
            delete_transaction(transactions)

        elif choice == "6":
            analyze_finances(transactions)

        elif choice == "7":
            save_transactions(transactions)

        # elif choice == "8":
            # generate_report(transactions)

        # elif choice == "9":
            # calculate_monthly_summary(transactions)

        elif choice == "10":
            view_transactions_from_file()

        elif choice == "11":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 11.")

# menu.py

from utils.analysis import (
    load_transactions,
    save_transactions,
    analyze_finances,
    generate_report,
    calculate_monthly_summary
)
from utils.transaction_ops import (
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    view_transactions_from_file,
    filter_transactions_by_year
)


# Global list to store the transactions in memory
transactions = []

def show_menu():
    """
    Display a text-based CLI menu and route the user's input to appropriate functions.
    The menu loops until the user chooses to exit.
    """
    global transactions

    while True:
        print("\n============================================="
              "\n====== SMART PERSONAL FINANCE ANALYZER ======"
              "\n=============================================")
        print("\n1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions (In Memory)")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Monthly Summary (Income, Expenses, Balance)")
        print("10. Filter Transactions by Year")  # Moved up
        print("11. View Transactions from File")
        print("12. Exit")  # Always last
        print("\n=============================================="
              "\n==============================================")
              

        choice = input("\nPlease Enter your choice (1–12): ").strip()

        if choice == "1":
            transactions = load_transactions()

        elif choice == "2":
            add_transaction(transactions)

        elif choice == "3":
            view_transactions(transactions)
            print("\n📄 Displayed all in-memory transactions.")

        elif choice == "4":
            update_transaction(transactions)

        elif choice == "5":
            delete_transaction(transactions)
        

        elif choice == "6":
            analyze_finances(transactions)
            print("\n 📊 Financial analysis complete.")

        elif choice == "7":
            save_transactions(transactions)

        elif choice == "8":
            generate_report(transactions)

        elif choice == "9":
            calculate_monthly_summary(transactions)

        elif choice == "10":
            filter_transactions_by_year(transactions)

        elif choice == "11":
            view_transactions_from_file()

        elif choice == "12":
            print("\n👋 Exiting the program. Goodbye!")
            break

        else:
            print("\n ⚠️ Invalid choice. Please enter a number between 1 and 12.")

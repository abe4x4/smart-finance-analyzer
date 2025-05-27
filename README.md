# Smart Personal Finance Analyzer

A modular Python CLI app to manage and analyze personal financial records.

## 🚧 Work in Progress

This project is currently under development.


➡️ STEP 1: Project Setup and First Commit
1. Create the project folder and essential subfolders. 
2. Initialize a Git repository and set up.
3. Create python virtual environment.
4. Create empty Python files for each module
5. Add .gitignore and a basic README.md
6. Stage, commit, and push this first commit to GitHub


➡️ STEP 2: Add load_transactions() and log_error() in finance_utils.py
1. Add the logic to load transactions from a CSV file
2. Add a helper function to log errors to errors.txt
3. Keep code modular and beginner-friendly
4. Update the README.md to reflect this functionality
5. Commit and push


➡️ STEP 3: Add save_transactions() to finance_utils.py to complete Task 5 (file saving). 
1. Add save_transactions() to finance_utils.py and Enhanced view_transactions() function
2. Link it to menu option 7 in menu.py
3. Ensure it runs from main.py
4. Update README.md
5. Stage, commit, and push to GitHub

➡️ STEP 4: Implemented Add and View FunctionalitySTEP 4: Implemented Add and View Functionality
1. add_transaction(): Allows users to input transaction details including date, amount, type, and description. Each new transaction is validated and assigned a unique ID.

2. view_transactions(): Displays the current list of transactions in a clear, formatted table. Debit amounts are shown in parentheses instead of with a minus sign, for professional readability.

3. view_transactions_from_file(): Added a separate menu option to display all transactions directly from the saved CSV file without affecting the in-memory list.

➡️ STEP 5: Implemented Update and Delete Functionality
1. update_transaction(): Lets users select a transaction by ID and update any field. Empty fields keep their original values. Includes validation for transaction types.

2. delete_transaction(): Lets users remove a transaction by ID, with full confirmation and a preview of the selected transaction.

➡️ STEP 6: Implemented Analysis Functionality
1. Total credits, total debits, and total transfers
2. Net balance (credits minus debits)
3. A breakdown of totals by transaction type








Fixed CSV file location and naming

Debugged empty loads by verifying the actual data

Implemented and validated a clean, formatted output of all file-based transactions

Confirmed your CLI option (10) is functional and professional

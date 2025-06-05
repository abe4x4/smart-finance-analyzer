# 💰 Smart Personal Finance Analyzer

A modular, beginner-friendly Python CLI application that helps users manage and analyze their personal financial transactions using CSV files.

This project was created as the Capstone Project for the Code You “Introduction to Python” course, and demonstrates real-world use of core Python concepts including file I/O, functions, lists, dictionaries, modules, conditionals, loops, and error handling.

---

## 📁 Project Structure  
smart-finance-analyzer/  
│  
├── data/                   # Contains the main CSV file and backups  
│   ├── financial_transactions.csv  
│   └── backup/  
│       └── financial_transactions_original.csv  
│  
├── utils/                  # Utility modules for finance and transaction logic  
│   ├── analysis.py         # File handling, loading/saving, reporting, summaries  
│   └── transaction_ops.py  # CRUD operations (add, update, delete, view)  
│  
├── reports/               # Stores generated financial summary reports  
│  
├── tests/                 # Placeholder for future unit tests  
│  
├── menu.py                # CLI menu logic that routes user input  
├── main.py                # Entry point that runs the program  
├── errors.txt             # Logs any CSV parsing or input errors  
└── README.md              # Project overview and development log  

---

## ✅ Completed Steps & Features

### ➡️ STEP 1: Project Setup and Initialization
- Created the project structure and folders  
- Initialized a Git repository  
- Set up a virtual environment  
- Created empty Python files for modular development  
- Added .gitignore and initial README  

### ➡️ STEP 2: Load Transactions and Log Errors
- Implemented `load_transactions()` to read a CSV file into memory  
- Used `datetime` for date parsing, and error handling with try-except blocks  
- Created `log_error()` logic to write issues to `errors.txt`  

### ➡️ STEP 3: Save Transactions to File
- Implemented `save_transactions()` to write the updated transaction list back to the CSV  
- Automatically backs up the original file before saving  

### ➡️ STEP 4: Add & View Transactions
- `add_transaction()`: lets the user add a new transaction with validation  
- `view_transactions()`: displays all current transactions with proper formatting  
- `view_transactions_from_file()`: reads directly from the CSV file to display saved transactions  

### ➡️ STEP 5: Update & Delete Transactions
- `update_transaction()`: allows users to edit specific fields in a selected transaction  
- `delete_transaction()`: deletes a transaction after confirmation  

### ➡️ STEP 6: Analyze Financial Data
- `analyze_finances()` calculates and prints:  
  - Total credits, debits, and transfers  
  - Net balance  
  - Breakdown of totals by transaction type  

### ➡️ STEP 7: Save and Generate Reports
- `save_transactions()` saves the current in-memory transactions to `financial_transactions.csv`  
- Automatically backs up the original CSV (if not already backed up) to `data/backup/`  
- `generate_report()` creates a summary report with totals, date range, and timestamp, and saves it to `reports/report_YYYYMMDD.txt`  

### ➡️ STEP 8: Monthly Summary
- `calculate_monthly_summary()` calculates and prints monthly totals of:  
  - Income (credit)  
  - Expenses (debit)  
  - Net balance  

---

## 📝 Git Commit Summary

- ✅ Step 1: Setup project, virtualenv, folders, README, and .gitignore  
- ✅ Step 2: Implemented transaction loader and error logger  
- ✅ Step 3: Added file-saving logic and CSV backup  
- ✅ Step 4: Add/view transactions from memory and file  
- ✅ Step 5: Add transaction update/delete functionality  
- ✅ Step 6: Implement financial summary logic  
- ✅ Step 7: Generate summary reports and save to file  
- ✅ Step 8: Monthly breakdown by income, expenses, and net  

---

## 📈 Upcoming Steps

- ➡️ Step 9: Optional Bonus Features (filters, year-specific analysis, type filtering, etc.)  
- ➡️ Step 10: Add unit tests inside the `tests/` folder  
- ➡️ Improve formatting, validations, and modularity for bonus round  

---

## 📌 Enhancements & Upgrades (Post Step 8)

The following improvements were added beyond the core 8-step project scope to increase functionality, user-friendliness, and code maintainability:

### ✅ Improved Transaction Entry
- When adding a new transaction:
  - Pressing Enter on the transaction ID auto-assigns the next available number.
  - Pressing Enter on the date auto-fills today’s date.
  - Pressing Enter on customer ID auto-assigns the next available customer ID.
  - Accepts shorthand input for transaction type:
    - 'c' = credit, 'd' = debit, 't' = transfer

### ✅ Safer and More User-Friendly Deletion
- delete_transaction():
  - Accepts both full (‘yes’, ‘no’) and shorthand (‘y’, ‘n’) confirmations
  - Reprompts user on invalid input with helpful guidance

### ✅ Analysis Output Cleanup
- Removed redundant summary from analyze_finances() that previously printed grouped totals twice

### ✅ Folder & Import Structure Improvements
- Merged all financial utilities and analysis logic into a single file: utils/analysis.py
- Updated all import statements and menu routing to reflect the new structure

### ✅ CLI Menu Enhancements
- The “Exit” option now always appears as the last option
- Menu restructured to improve logical grouping and match project milestones
- Bonus feature: View transactions directly from the file remains available and properly routed

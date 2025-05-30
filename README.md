# 💰 Smart Personal Finance Analyzer

A modular, beginner-friendly Python CLI application that helps users manage and analyze their personal financial transactions using CSV files.

This project was created as the Capstone Project for the Code You “Introduction to Python” course, and demonstrates real-world use of core Python concepts including file I/O, functions, lists, dictionaries, modules, conditionals, loops, and error handling.

---

## 📁 Project Structure  
smart-finance-analyzer/  
│  
├── data/ # Contains the main CSV file and backups  
│ ├── financial_transactions.csv  
│ └── backup/  
│ └── financial_transactions_original.csv  
│  
├── utils/ # Utility modules for finance and transaction logic  
│ ├── finance_utils.py  
│ └── transaction_ops.py  
│
├── tests/ # Placeholder for future test files  
│  
├── menu.py # CLI menu logic that routes user input  
├── main.py # Entry point that runs the program  
├── analysis.py # Contains financial summary logic  
├── errors.txt # Logs any CSV parsing or input errors  
└── README.md # Project overview and development log  




## ✅ Completed Steps & Features

### ➡️ STEP 1: Project Setup and Initialization
- Created the project structure and folders
- Initialized a Git repository
- Set up a virtual environment
- Created empty Python files for modular development
- Added .gitignore and initial README

### ➡️ STEP 2: Load Transactions and Log Errors
- Implemented load_transactions() to read a CSV file into memory
- Used datetime for date parsing, and error handling with try-except blocks
- Created log_error() logic to write issues to errors.txt

### ➡️ STEP 3: Save Transactions to File
- Implemented save_transactions() to write the updated transaction list back to the CSV
- Automatically backs up the original file before saving

### ➡️ STEP 4: Add & View Transactions
- add_transaction(): lets the user add a new transaction with validation
- view_transactions(): displays all current transactions with proper formatting
- view_transactions_from_file(): reads directly from the CSV file to display saved transactions

### ➡️ STEP 5: Update & Delete Transactions
- update_transaction(): allows users to edit specific fields in a selected transaction
- delete_transaction(): deletes a transaction after confirmation

### ➡️ STEP 6: Analyze Financial Data
- analyze_finances(): Calculates and prints:
  - Total credits, debits, and transfers
  - Net balance
  - Breakdown of totals by transaction type

---

## 📝 Git Commit Summary

- ✅ Step 1: Setup project, virtualenv, folders, README, and .gitignore
- ✅ Step 2: Implemented transaction loader and error logger
- ✅ Step 3: Added file-saving logic and CSV backup
- ✅ Step 4: Add/view transactions from memory and file
- ✅ Step 5: Add transaction update/delete functionality
- ✅ Step 6: Implement financial summary report

---

## 🚧 Upcoming Steps

- Step 7: Generate reports and summaries
- Step 8: Implement monthly summary breakdown
- Step 9: Optional Bonus Features (filters, year analysis, etc.)
- Add unit tests to /tests folder

---

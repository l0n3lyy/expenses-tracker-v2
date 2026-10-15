# 💰 Expense Tracker

A simple command-line expense tracker built with Python. It allows users to record expenses, view their spending history, and calculate total expenses.

## ✨ Features

- **Add expenses** — enter an expense name, category, and amount.
- **View expenses** — display all recorded expenses.
- **Calculate total expenses** — automatically calculate the total amount spent.
- **Delete expenses** — remove a selected expense by its number.
- **Data persistence** — expenses are saved to `expenses.json` and remain available after restarting the program.
- **Automatic data loading** — previously saved expenses are loaded when the program starts.
- **Input validation** — if the user enters text instead of a number, the program displays an error and asks for the amount again without crashing.

## 🆕 What's New in This Version

- Added error handling for expense amounts using `try/except ValueError`.
- Implemented repeated input until a valid numeric amount is entered.
- Added a Boolean flag using `True` and `False` to track whether the input is valid.
- Improved protection against invalid user input.

## 🛠️ Technologies Used

- **Python**
- `json` — for saving and loading expense data.
- `pathlib` — for checking whether a file exists.
- `try/except` — for handling input errors.
- `while` — for loops and repeated input.
- `list` and `dict` — for storing expense information.

## 🚀 How to Run

1. Install Python.
2. Download the `expense_tracker.py` file.
3. Open a terminal in the project directory.
4. Run the following command:

   ```bash
   python expense_tracker.py
   ```

The `expenses.json` file is created automatically if it does not already exist.

## 📚 Project Goals

This project was created to practice Python and learn about functions, loops, data structures, error handling, and JSON data persistence.

The project is continuously evolving as new Python concepts are learned and new features are implemented.

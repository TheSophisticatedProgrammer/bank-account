# Simple CLI Banking System

A terminal-based Python application that simulates basic banking operations. You can use to learn and build on this project.

## Features

- **Account Tracking**: Stores account holder names, current balances, and lockout status.
- **Transactions**: Facilitates deposits, withdrawals, and transfers between accounts.
- **Security Simulation**: Implements a lockout counter for failed withdrawal attempts.
- **Access Recovery**: Features an unlock command to restore access to locked accounts.

## Prerequisites

- Python 3.x

## How to Run

1. Save the code to a file named `bank_system.py`.
2. Open a terminal.
3. Execute the script:

## Usage Guide

Available actions in the command menu:

* **create**: Register a new account name.
* **deposit**: Increase the balance of a specified account.
* **withdraw**: Decrease the balance of an account. Note that repeated insufficient funds attempts will lock the account.
* **transfer**: Move money from one account name to another.
* **unlock**: Use the system credential to reactivate a locked account.
* **quit**: Terminate the program.

## System Architecture

* **Class BankAccount**: The data structure for individual user records.
* **Global Accounts Dictionary**: The primary storage for all account objects during runtime.
* **Action Dispatcher**: A dictionary-based routing system that connects user input to specific functions.

# Python Mini POS System

A simple command-line Point of Sale (POS) application developed in Python to practice programming fundamentals and basic retail transaction logic.

## Features

- Search for products by name
- Calculate item subtotals and total purchase amounts
- Validate product quantities and available stock
- Prevent duplicate cart entries from exceeding available stock
- Handle invalid numeric inputs
- Validate customer payments and calculate change
- Update inventory after successful payment

## Technologies Used

- Python 3
- Lists and Dictionaries
- Functions and Loops
- Conditional Statements
- Exception Handling

## How to Run

1. Install Python 3.
2. Download the `Mini_POS.py` file.
3. Open a terminal in the project folder.
4. Run:

   `python Mini_POS.py`

5. Enter a product name and quantity. Type `exit` to finish selecting products and proceed to payment.

## Available Products

| Product | Price (THB) | Initial Stock |
|---|---:|---:|
| Coffee | 70 | 10 |
| Tea | 55 | 8 |
| Cake | 120 | 5 |

## Example Transaction

- Coffee x 2 = 140 THB
- Tea x 1 = 55 THB
- Total = 195 THB
- Customer Payment = 200 THB
- Change = 5 THB

## Project Limitations

- Supports one customer transaction per program run.
- Inventory is stored in memory and resets when the program restarts.
- No database or persistent sales history is included.

## Learning Outcomes

This project helped me practice Python fundamentals, data structures, input validation, and business logic through a retail transaction scenario.

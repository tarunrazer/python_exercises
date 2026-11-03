# exercises/01_w3_variables.py
"""
W3Schools Python Syntax & Variables Practice
Verify local environment execution and basic data types.
"""

def practice_variables():
    # 1. Variables and Types
    item_name = "Enterprise License"
    quantity = 5
    unit_price = 199.99
    is_active = True

    # 2. String Formatting & Arithmetic
    total_cost = quantity * unit_price
    summary = f"Item: {item_name} | Qty: {quantity} | Total: ${total_cost:.2f}"

    print("--- W3Schools Exercise 01 ---")
    print(summary)
    print("Data Types:", type(item_name), type(quantity), type(unit_price), type(is_active))

if __name__ == "__main__":
    practice_variables()
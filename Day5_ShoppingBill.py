def shopping_bill():
    print("=== Shopping Bill Calculator ===")

    # Get prices of 3 items
    item1 = float(input("Enter the price of item 1: ₹"))
    item2 = float(input("Enter the price of item 2: ₹"))
    item3 = float(input("Enter the price of item 3: ₹"))

    # Get tax percentage
    tax_percent = float(input("Enter tax percentage (e.g., 5 for 5%): "))

    # Calculate subtotal
    subtotal = item1 + item2 + item3

    # Calculate tax and total
    tax_amount = (tax_percent / 100) * subtotal
    total = subtotal + tax_amount

    # Print formatted bill
    print("\n--- BILL ---")
    print(f"Item 1: ₹{item1:.2f}")
    print(f"Item 2: ₹{item2:.2f}")
    print(f"Item 3: ₹{item3:.2f}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
    print(f"Total Amount: ₹{total:.2f}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    shopping_bill()

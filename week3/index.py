def calculate_discount(price, discount_percent):
    
    # Calculates the final price after applying a discount.
    # If discount_percent >= 20, apply the discount.
    # Otherwise, return the original price.
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    # Check if discount was applied
    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")

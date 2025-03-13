"""Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price."""

def calculate_discount(price, discount_percent):
    """function to calculate discount"""
    try:
        price = float(price)
        discount_percent = float(discount_percent)
        if discount_percent >= 20:
            discount = price * (discount_percent/100)
            return price - discount  #Final price with discount applied
        else:
            return price # final price without discount
    except ValueError as e:
        return f"valueError: {e}"
    except TypeError as e:
        return f"Type error : {e}"
    
#collecting user input
price = input('Enter The original price: ')
discount_percent = input('Enter The discount percentage: ')

calculate_discount(price,discount_percent)
print(f'Final price: {calculate_discount(price,discount_percent)}')
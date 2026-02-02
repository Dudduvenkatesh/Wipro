
import random
products = {}
def add_products():
    n = int(input("Enter number of products to add: "))
    for i in range(n):
        name = input(f"Enter product {i+1} name: ")
        price = int(input(f"Enter price of {name}: "))
        products[name] = price
def validate_quantity(qty):
    return qty > 0

def calculate_total(price, quantity):
    return price * quantity

def generate_order_id():
    return f"{random.randint(1000, 9999)}"
def place_order():
    print("\n===== E-COMMERCE ORDERING SYSTEM =====\n")

    print("Available Products:")
    for item, price in products.items():
        print(f"{item} - ₹{price}")
    while True:
        product = input("\nEnter product name: ")
        if product in products:
            break
        else:
            print("Product not available. Please enter again.")
    while True:
        quantity = int(input("Enter quantity: "))
        if validate_quantity(quantity):
            break
        else:
            print("Invalid quantity. Enter quantity greater than 0.")

    total = calculate_total(products[product], quantity)
    order_id = generate_order_id()

    print("\n========== ORDER DETAILS ==========")
    print(f"Order ID : {order_id}")
    print(f"Product  : {product}")
    print(f"Quantity : {quantity}")
    print(f"Total ₹  : {total}")
    print("Order placed successfully!")
    print("Thank you for shopping with us!")
add_products()
place_order()

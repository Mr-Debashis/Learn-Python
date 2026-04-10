
# Restaurant menu
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Welcome customers 
print('Welcome to CoCo Restaurant')

# Show menu to user using loop
for key, value in menu.items():
    print(f"{key} Rs-{value}")

# Define this to hold user input values
total_order_amount = 0
total_order_item = []

# User give order using this input
user_fast_input = input('What you like to order!\nEnter the name of item you want to order : ')

# Check user input with menu
if user_fast_input in menu:
    total_order_amount += menu[user_fast_input]
    total_order_item.append((user_fast_input, menu[user_fast_input]))
    print(f"Your item {user_fast_input} has been added to cart")
else:
    print(f"Ordered item {user_fast_input} is not available!")

# User give another order using this input
user_second_input = input("Do you want to order another item ? (Yes/No) : ")

if user_second_input == 'Yes':
    user_third_input = input("Enter the name of the item you want to add : ")
    if user_third_input in menu:
        total_order_amount += menu[user_third_input]
        total_order_item.append((user_third_input, menu[user_third_input]))
        print(f"Your item {user_third_input} has been added to cart")
    else:
        print(f"Ordered item {user_third_input} is not available!")

print("\nYour ordered items are:")
for item, price in total_order_item:
    print(f"{item} Rs-{price}")
print(f"\nTotal amount: Rs {total_order_amount}")

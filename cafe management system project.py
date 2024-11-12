menu = {
    'Pizza': 50,
    'Burger': 60,
    'Coffee': 70,
    'Maggi': 30,
}

print("Welcom to btech cafe")
print("Pizza: Rs50\nBurger: 60\nCoffee: 70\nMaggi: 30")

order_total=0

item_1 = input("Enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been order")
else:
    print(f"Ordered item is unavailable")
another_item = input("Do you want to add another item? (Yes/No)") 
if another_item=="Yes":
    item_2 = input("Enter the name of second item:")
if item_2 in menu:
    order_total += menu[item_2]    
    print(f"Item {item_2} has been added to order")
else:
    print(f"Ordered item {item_2} is not available:")

print(f"The total amount of items to pay is {order_total}")



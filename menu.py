import os
os.system('cls')

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Desserts": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

# print(menu)
# print(menu.items())

# Launch the store and present a greeting to the customer
print("\nWelcome to the Variety Food Truck.\n")

# Customers may want to order multiple items, so let's create a continuous
# loop
# Starting with an empty Order
order = {}
z = 0
place_order = True
while place_order:

    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order?")

    # Create a variable for the menu item number
    i = 1

    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for category in menu.keys():
        print(f"{i}: {category}")

        # Store the menu category associated with its menu item number
        menu_items[i] = category

        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("\nSelect a menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():

        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_selection)]

            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}\n")

            # Print out the menu options from the menu_category_name
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary and display sub-items
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                # if not, handle as a single item
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_item_selection = input(
                f"\nWhat item from the {menu_category_name} menu would you like to order? ")

            # 3. Check if the customer typed a number
            if menu_item_selection.isdigit():
               
                # Convert the menu selection to an integer
                menu_item_selection = int(menu_item_selection)
                
                # 4. Check if the menu selection is in the menu items
                for key, value in menu_items.items():
                    if key == menu_item_selection:
                        # print(key, value["Item name"], value["Price"])

                        # Store the item name as a variable
                        menu_selection_name = value["Item name"]
                        price_ea = value["Price"]

                        # Ask the customer for the quantity of the menu item
                        quantity = input(
                            f"\nHow many orders of {menu_selection_name} at ${price_ea} ea. would you like to order? ")

                        # Check if the quantity is a number, default to 1 if not
                        if quantity.isdigit():
                            if quantity == 0:
                                print("\nLets restart from the beginning.")
                                break
                            else:
                                quantity = int(quantity)
                        else:
                            quantity = int(1)
                            print(f"\nInvalid entry, defaulting quantity to: {quantity}")
                                                
                        # Add the item name, price, and quantity to the order list
                        order_list = {menu_selection_name, price_ea, quantity}
                        total_cost = quantity * float(price_ea)

                        print("\nYou have submitted the following order:")
                        print("---------------------------------------")
                        print(f"{menu_category_name}: {menu_selection_name} - Qty: {quantity} = ${total_cost:.2f}")
                        print()
                        # print(order_list)
                        # place_order = False
                        
                        # Create Order and append to it any additional orders
                        z = z + 1
                        order[z] = {"Item name": menu_selection_name, "Price": price_ea, "Quantity": quantity}
                        # print(order)
                    
                # Tell the customer that their input isn't valid
                print(f"{menu_item_selection} is not a valid selection.")
                    
            # Tell the customer they didn't select a menu option
            else:
                print(f"{menu_item_selection} is not a valid choice.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # while True:
    # Ask the customer if they would like to order anything else
    keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ")

    # 5. Check the customer's input
    if keep_ordering.lower() == "y":
        
        # Keep ordering
        place_order = True
        
    # Exit the keep ordering question loop
    else:
        place_order = False

    # Complete the order

        # Since the customer decided to stop ordering, thank them for
        # their order
print("\nThank you for ordering from the Variety Food Truck.")
        # Exit the keep ordering question loop

        # Tell the customer to try again

# Print out the customer's order
print("\nPlease confirm the following is your order.\n")

# Uncomment the following line to check the structure of the order
#print(order)
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

#for orders, items in order.items():
#    for item in items.values():
#        print(item)
for orders in order.values():

    # 7. Store the dictionary items as variables
    items = orders["Item name"]
    prices = orders["Price"]
    quantities = orders["Quantity"]
  
    # 8. Calculate the number of spaces for formatted printing
    
    # 9. Create space strings

    # 10. Print the item name, price, and quantity
    print(f"{items:<25} | ${prices:>5.2f} | {quantities:>4}")

confirm = input("\nConfirm order? (Y/N): ")
if confirm == "Y" or "y":
    os.system('cls')
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for orders in order.values():
        items = orders["Item name"]
        prices = orders["Price"]
        quantities = orders["Quantity"]
        print(f"{items:<25} | ${prices:>5.2f} | {quantities:>4}")
#print()
#print(order)
#print()        
# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

print("--------------------------|--------|----------")
total_price = sum(order[key]["Price"] * order[key]["Quantity"] for key in order)
print(f"Total due:                | ${total_price:5.2f} |\n")

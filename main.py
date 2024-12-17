import os
currentdir = os.getcwd()
file_path = f'{currentdir}/inventory.txt'
print(f"Currently using file path: {file_path}")

dataFile = open(file_path, 'a+')
with open(file_path, 'r+') as readFile:
    dataFileContents = [line.strip() for line in readFile]
    readFile.close()
def add_item(name, price, quantity):
    """
    Adds an item to the inventory file with the specified name, price, and quantity.
    
    Args:
        name (str): The name of the item
        price (float): The price of the item in USD
        quantity (int): The amount of the item currently in inventory
    """
    with open(file_path, 'a') as dataFile:
        dataFile.write(f"{name},{quantity},{price}\n")
    return f"Successfully added item {name}."

def remove_item(name):
    """
    Removes an item from the inventory file.
    
    Args:
        name (str): The name of the item to be removed
    """
    if len(dataFileContents) == 0:
        return "0 items found in file. Add items before trying to delete."
    for item in dataFileContents:
        fullItem = item
        item = item.split(',')
        print(item)
        if item[0] == name:
            dataFileContents.remove(fullItem)
            for item in dataFileContents:
                dataFile.write(item)
            return f"Successfully deleted {name}."
    return f"{name} not found in inventory. Please check spelling and try again."

def update_item(name, quantity):
    """
    Updates an item's quantity from their name.
    
    Args:
        name (str): The name of the item to be updated
        quantity (int): The new quantity of the item
    """
    if len(dataFileContents) < 0:
        return "0 items found in file. Add items before trying to update."
    for item in dataFileContents:
        item = item.split(',')
        if item[0] == name:
            item[1] = quantity
            for item in dataFileContents:
                dataFile.write(item)
            return f"Successfully updated {name}."
    return f"{name} not found in inventory. Please check spelling and try again."

def display():
    """
    Displays the inventory stock in an orderly fashion.
    """
    print("\nInventory Stock")
    if len(dataFileContents) < 1:
        print("No items in file. Add items and try again.")
        return
    else:
        for item in dataFileContents:
           item = item.split(',')
           print(f"Name: {item[0]} | Quantity: {item[1]} | Price: {item[2]}\n")

def showItem(name):
    """
    Displays a single item and it's quantity from the name
    
    Args:
        name (str): The name of the item to be displayed
    """
    if len(dataFileContents) < 0:
        return "0 items found in file. Add items before trying to searcb."
    for item in dataFileContents:
        item = item.split(',')
        if item[0] == name:
            print(f"Name: {item[0]} | Quantity: {item[1]} | Price: {item[2]}\n")
            return
    return f"{name} not found in inventory. Please check spelling and try again."

def inputCheck(msg,typeIn='str'):
    """
    This function loops for user input until a proper input is entered using try and except.
    """
    while True:
        if typeIn == 'int':
            try:
                userInput = int(input(f"[?] {msg}"))
                return userInput
            except ValueError:
                print("Invalid input. Try again.")
                pass
        elif typeIn == 'str':
             try:
                userInput = input(f"[?] {msg}")
                return userInput
             except ValueError:
                print("Invalid input. Try again.")
                pass
        elif typeIn == 'float':
             try:
                userInput = float(input(f"[?] {msg}"))
                return userInput
             except ValueError:
                print("Invalid input. Try again.")
                pass

print("Inventory Program\n")
while True:
    print("OPTIONS:\n1. Add Item\n2. Remove Item\n3.Update Item\n4. Display Single Item\n5. Display Inventory\n6. Exit Program")
    option = inputCheck("Enter a number (1-6): ", 'int')
    while option < 1 or option > 6:
        print("Invalid menu option. Please enter a number 1-6.")
        option = inputCheck("Enter a number (1-6): ", 'int')
    if option == 1:
        name = inputCheck("Enter the name of the item: ")
        price = inputCheck("Enter the price of the item: ", 'float')
        quantity = inputCheck("Enter the quantity of the item: ", 'int')
        print(add_item(name, price, quantity))
    elif option == 2:
        name = inputCheck("Enter the name of the item: ")
        print(remove_item(name))
    elif option == 3:
        name = inputCheck("Enter the name of the item: ")
        quantity = inputCheck("Enter the new desired quantity of the item: ", 'int')
        print(update_item(name, quantity))
    elif option == 4:
        name = inputCheck("Enter the name of the item: ")
        print(showItem(name))
    elif option == 5:
        display()
    elif option == 6:
        break

dataFile.close()

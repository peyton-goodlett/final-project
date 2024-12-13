file_path = 'C:/Users/015GOODLEPS/OneDrive - Carroll County KY Schools/Desktop/side/inventory.txt'
# File format: itemName,quantity,price
dataFile = open(file_path, 'a+')
dataFileContents = open(file_path, 'r+').read()
def add_item(name, price, quantity):
    """
    Adds an item to the inventory file with the specified name, price, and quantity.
    
    Args:
        name (str): The name of the item
        price (float): The price of the item in USD
        quantity (int): The amount of the item currently in inventory
    """
    with open(file_path, 'a') as dataFile:
        dataFile.append(f"{name},{price},{quantity}")
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
        if item[0] == name:
            dataFileContents.remove(item)
            for item in dataFileContents:
                dataFile.write(item)
            return f"Successfully deleted {name}."
    return f"{name} not found in inventory. Please check spelling and try again."

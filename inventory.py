inventory = [
    {
        "id": 1,
        "barcode": "737628064502",
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 4.50,
        "stock": 20,
        "category": "Beverages"
    },
    {
        "id": 2,
        "barcode": "3017620422003",
        "product_name": "Nutella",
        "brand": "Ferrero",
        "price": 6.99,
        "stock": 15,
        "category": "Spread"
    },
    {
        "id": 3,
        "barcode": "5449000000996",
        "product_name": "Coca-Cola",
        "brand": "Coca-Cola",
        "price": 2.50,
        "stock": 30,
        "category": "Soft Drinks"
    }
]

def get_all_items():
    """
    Returns the complete inventory.
    """
    return inventory

def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None

def add_item(item):
    if inventory:
        new_id = inventory[-1]["id"] + 1
    else:
        new_id = 1

    item["id"] = new_id
    inventory.append(item)

    return item

def update_item(item_id, updates):
    """
    Updates only the fields provided.
    """

    item = get_item(item_id)

    if item is None:
        return None

    item.update(updates)

    return item

def delete_item(item_id):
    """
    Removes an item from the inventory.
    """

    item = get_item(item_id)

    if item is None:
        return False

    inventory.remove(item)

    return True
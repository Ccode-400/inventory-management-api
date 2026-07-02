import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        if not items:
            print("\nInventory is empty.\n")
            return

        print("\n===== INVENTORY =====")

        for item in items:
            print(f"""
ID: {item['id']}
Name: {item['product_name']}
Brand: {item['brand']}
Price: ${item['price']}
Stock: {item['stock']}
Category: {item['category']}
Barcode: {item['barcode']}
-----------------------------
""")
    else:
        print("Error retrieving inventory.")

def view_item():

    item_id = input("Enter Item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:

        item = response.json()

        print("\n===== ITEM DETAILS =====")

        for key, value in item.items():
            print(f"{key}: {value}")

    else:
        print("Item not found.")

def add_item():
    data = {
        "barcode": input("Barcode: "),
        "product_name": input("Product Name: "),
        "brand": input("Brand: "),
        "price": float(input("Price: ")),
        "stock": int(input("Stock: ")),
        "category": input("Category: ")
    }
    
    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    if response.status_code == 201:
        print("\nItem added successfully!\n")
    else:
        print(response.json())

def update_item():
    item_id = input("Item ID: ")
    print("\nLeave blank if you don't want to update a field.\n")
    updates = {}
    price = input("New Price: ")

    if price:
        updates["price"] = float(price)
        stock = input("New Stock: ")

    if stock:
        updates["stock"] = int(stock)
        category = input("New Category: ")

    if category:
        updates["category"] = category

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=updates
    )

    if response.status_code == 200:
        print("Item updated successfully.")
    else:
        print("Item not found.")

def delete_item():
    item_id = input("Item ID: ")
    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print("Item deleted.")
    else:
        print("Item not found.")

def search_api():
    barcode = input("Enter Barcode: ")
    response = requests.get(
        f"{BASE_URL}/search/{barcode}"
    )

    if response.status_code == 200:
        product = response.json()
        print("\n===== PRODUCT FOUND =====\n")
        for key, value in product.items():
            print(f"{key}: {value}")
    else:
        print("Product not found.")

def import_product():
    barcode = input("Barcode: ")
    response = requests.post(
        f"{BASE_URL}/import/{barcode}"
    )

    if response.status_code == 201:
        print("\nProduct imported into inventory!")
        print(response.json())
    else:
        print("Could not import product.")

def menu():
    while True:
        print("""
==============================
Inventory Management System
==============================

1. View Inventory

2. View Item

3. Add Item

4. Update Item

5. Delete Item

6. Search OpenFoodFacts

7. Import Product

8. Exit

==============================
""")

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            search_api()

        elif choice == "7":
            import_product()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    menu()
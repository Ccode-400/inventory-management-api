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


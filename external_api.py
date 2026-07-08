import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0 (student project)"
}


def fetch_product(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown Product"),
            "brand": product.get("brands", "Unknown Brand"),
            "ingredients": product.get("ingredients_text", ""),
            "category": product.get("categories", ""),
            "image": product.get("image_url", "")
        }

    except requests.RequestException as e:
        print(e)
        return None
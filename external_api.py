import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def fetch_product(barcode):
    """
    Fetch product details from OpenFoodFacts using a barcode.

    Args:
        barcode (str): Product barcode.

    Returns:
        dict: Product information if found.
        None: If product does not exist or request fails.
    """

    url = f"{BASE_URL}/{barcode}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        if data.get("status") == 1:

            product = data.get("product", {})

            return {
                "barcode": barcode,
                "product_name": product.get("product_name", "Unknown Product"),
                "brand": product.get("brands", "Unknown Brand"),
                "ingredients": product.get("ingredients_text", "Not Available"),
                "category": product.get("categories", "Unknown"),
                "image": product.get("image_url", "")
            }





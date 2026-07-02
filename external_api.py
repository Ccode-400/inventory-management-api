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


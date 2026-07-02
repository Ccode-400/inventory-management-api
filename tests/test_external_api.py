from unittest.mock import patch
from external_api import fetch_product

@patch("external_api.requests.get")
def test_fetch_product_success(mock_get):

    mock_response = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "ingredients_text": "Filtered water, almonds",
            "categories": "Plant-based foods",
            "image_url": "https://example.com/image.jpg"
        }
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    product = fetch_product("737628064502")

    assert product is not None
    assert product["product_name"] == "Organic Almond Milk"
    assert product["brand"] == "Silk"
    assert product["category"] == "Plant-based foods"

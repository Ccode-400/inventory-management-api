import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from unittest.mock import patch, Mock
import cli

@patch("cli.requests.get")
def test_view_inventory(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": 1,
            "barcode": "123",
            "product_name": "Milk",
            "brand": "Silk",
            "price": 4.50,
            "stock": 10,
            "category": "Dairy"
        }
    ]

    mock_get.return_value = mock_response
    cli.view_inventory()
    mock_get.assert_called_once()

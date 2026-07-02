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

@patch("cli.requests.get")
@patch("builtins.input", return_value="737628064502")
def test_search_api(mock_input, mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "product_name": "Organic Almond Milk",
        "brand": "Silk"
    }

    mock_get.return_value = mock_response
    cli.search_api()
    mock_get.assert_called_once()

@patch("cli.requests.post")
@patch("builtins.input", return_value="737628064502")
def test_import_product(mock_input, mock_post):
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "id": 4,
        "product_name": "Organic Almond Milk"
    }

    mock_post.return_value = mock_response
    cli.import_product()
    mock_post.assert_called_once()

@patch("cli.requests.delete")
@patch("builtins.input", return_value="1")
def test_delete_item(mock_input, mock_delete):
    mock_response = Mock()
    mock_response.status_code = 200

    mock_delete.return_value = mock_response
    cli.delete_item()
    mock_delete.assert_called_once()
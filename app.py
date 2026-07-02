from flask import Flask, jsonify, request

from inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item,
)

from external_api import fetch_product

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_inventory():
    """
    Return all inventory items.
    """
    return jsonify(get_all_items()), 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):

    item = get_item(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200

@app.route("/inventory", methods=["POST"])
def create_item():

    data = request.get_json()

    required_fields = [
        "barcode",
        "product_name",
        "brand",
        "price",
        "stock",
        "category",
    ]



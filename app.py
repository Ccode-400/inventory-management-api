from flask import Flask, jsonify, request

from inventory import (get_all_items, get_item, add_item, update_item, delete_item)

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

    required_fields = ["barcode", "product_name", "brand", "price", "stock", "category"]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_item = add_item(data)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def edit_item(item_id):

    data = request.get_json()

    updated = update_item(item_id, data)

    if updated is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(updated), 200

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):

    deleted = delete_item(item_id)

    if not deleted:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": "Item deleted successfully"}), 200

@app.route("/search/<barcode>", methods=["GET"])
def search_product(barcode):

    product = fetch_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200

@app.route("/import/<barcode>", methods=["POST"])
def import_product(barcode):

    product = fetch_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    inventory_item = {
        "barcode": product["barcode"],
        "product_name": product["product_name"],
        "brand": product["brand"],
        "price": 0.00,
        "stock": 0,
        "category": product["category"],
    }

    added_item = add_item(inventory_item)

    return jsonify(added_item), 201

@app.route("/", methods=["GET"])
def home():

    return jsonify(
        {
            "message": "Inventory Management API",
            "routes": [
                "GET /inventory",
                "GET /inventory/<id>",
                "POST /inventory",
                "PATCH /inventory/<id>",
                "DELETE /inventory/<id>",
                "GET /search/<barcode>",
                "POST /import/<barcode>",
            ],
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
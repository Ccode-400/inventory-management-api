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
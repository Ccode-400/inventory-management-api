# Inventory Management System REST API

## Overview

The Inventory Management System is a Python-based REST API built using Flask. It allows employees to manage inventory through Create, Read, Update, and Delete (CRUD) operations. The application also integrates with the OpenFoodFacts API to retrieve product information using a barcode. A command-line interface (CLI) is included to allow users to interact with the API without using Postman.

# Features

* RESTful Flask API
* Full CRUD functionality
* Mock inventory database using a Python list
* OpenFoodFacts API integration
* Command-Line Interface (CLI)
* Unit testing using Pytest
* External API testing using unittest.mock
* Error handling for invalid requests
* Well-structured and documented code

---

# Technologies Used

* Python 3
* Flask
* Requests
* Pytest
* unittest.mock
* Git & GitHub

---

# Project Structure

```text
inventory-management-api/
│
├── app.py
├── inventory.py
├── external_api.py
├── cli.py
├── requirements.txt
├── README.md
│
└── tests/
    ├── test_api.py
    ├── test_external_api.py
    └── test_cli.py
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/inventory-management-api.git
```

Replace **YOUR_USERNAME** with your GitHub username.

---

## 2. Navigate into the project

```bash
cd inventory-management-api
```

---


## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Flask API

Start the Flask server by running:

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

# Running the CLI

Open a second terminal while the Flask API is running.

Run:

```bash
python cli.py
```

The CLI menu will appear:

```
Inventory Management System

1. View Inventory
2. View Item
3. Add Item
4. Update Item
5. Delete Item
6. Search OpenFoodFacts
7. Import Product
8. Exit
```

---

# API Endpoints

| Method | Endpoint          | Description                                        |
| ------ | ----------------- | -------------------------------------------------- |
| GET    | /                 | Home route                                         |
| GET    | /inventory        | Retrieve all inventory items                       |
| GET    | /inventory/<id>   | Retrieve a single inventory item                   |
| POST   | /inventory        | Add a new inventory item                           |
| PATCH  | /inventory/<id>   | Update an inventory item                           |
| DELETE | /inventory/<id>   | Delete an inventory item                           |
| GET    | /search/<barcode> | Search OpenFoodFacts by barcode                    |
| POST   | /import/<barcode> | Import a product from OpenFoodFacts into inventory |

---

# Example API Requests

## Get All Inventory

```
GET /inventory
```

---

## Get One Item

```
GET /inventory/1
```

---

## Add New Item

```
POST /inventory
```

Request Body

```json
{
    "barcode":"123456789",
    "product_name":"Bread",
    "brand":"Sunrise",
    "price":3.99,
    "stock":20,
    "category":"Bakery"
}
```

---

## Update Item

```
PATCH /inventory/1
```

Request Body

```json
{
    "price":5.99,
    "stock":50
}
```

---

## Delete Item

```
DELETE /inventory/1
```

---

## Search OpenFoodFacts

```
GET /search/737628064502
```

---

## Import Product

```
POST /import/737628064502
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_api.py
```

Verbose mode:

```bash
pytest -v
```

---

# OpenFoodFacts API

This application uses the OpenFoodFacts API to retrieve product information using a barcode.

Information retrieved includes:

* Product Name
* Brand
* Ingredients
* Category
* Product Image URL

If the barcode does not exist or the API is unavailable, the application returns an appropriate error message.

---

# Error Handling

The application handles:

* Invalid inventory IDs
* Missing required fields
* Product not found
* API connection failures
* Invalid user input

---

# Future Improvements

Potential enhancements include:

* Replace the mock list with a SQLite or PostgreSQL database.
* Add user authentication and authorization.
* Implement product search by name.
* Add pagination for large inventories.
* Build a web-based frontend using HTML/CSS/JavaScript or React.
* Add Docker support for easier deployment.

---
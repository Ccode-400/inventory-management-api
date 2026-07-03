# Inventory Management System

## Overview

This project is a full-stack Inventory Management System developed using **Python Flask** for the backend and **React (Vite)** for the frontend. It allows administrators to manage inventory items through a REST API, a command-line interface (CLI), and a modern web interface.

The system also integrates with the **OpenFoodFacts API** to retrieve product information using a barcode.

---

## Features

### Backend (Flask REST API)

- View all inventory items
- View a single inventory item
- Add new inventory items
- Update existing inventory items
- Delete inventory items
- Search products using the OpenFoodFacts API
- Import products directly into the inventory

### Frontend (React + Vite)

- Display inventory items
- Add new inventory items
- Edit inventory items
- Delete inventory items
- Search products by barcode
- Import products from OpenFoodFacts
- Automatically refresh inventory after changes

### Command Line Interface

- View inventory
- Add inventory items
- Update stock and prices
- Delete inventory items
- Search OpenFoodFacts
- Import products

### Testing

- Flask API endpoint tests
- CLI tests
- External API tests using mocked responses

---

# Technologies Used

## Backend

- Python 3
- Flask
- Flask-CORS
- Requests
- Pytest

## Frontend

- React
- Vite
- Axios

## External API

- OpenFoodFacts API

---

# Project Structure

```
inventory-management-api/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AddItem.jsx
│   │   │   ├── InventoryList.jsx
│   │   │   ├── SearchProduct.jsx
│   │   │   └── UpdateItem.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── tests/
│   ├── test_api.py
│   ├── test_cli.py
│   └── test_external_api.py
│
├── app.py
├── cli.py
├── external_api.py
├── inventory.py
├── requirements.txt
├── Pipfile
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

```bash
cd inventory-management-api
```

---

# Backend Setup

Create a virtual environment.

```bash
python3 -m venv venv
```

Activate it.

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask flask-cors requests pytest
```

---

# Start the Flask Server

```bash
python app.py
```

The API will run on:

```
http://127.0.0.1:5000
```

---

# Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start the React application.

```bash
npm run dev
```

The frontend will run on:

```
http://localhost:5173
```

---

# API Endpoints

## Inventory

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /inventory | Get all inventory items |
| GET | /inventory/<id> | Get a single inventory item |
| POST | /inventory | Add a new item |
| PATCH | /inventory/<id> | Update an item |
| DELETE | /inventory/<id> | Delete an item |

---

## OpenFoodFacts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /search/<barcode> | Search product by barcode |
| POST | /import/<barcode> | Import product into inventory |

---

# Example JSON

```json
{
    "barcode": "737628064502",
    "product_name": "Organic Almond Milk",
    "brand": "Silk",
    "price": 4.99,
    "stock": 20,
    "category": "Beverages"
}
```

---

# Running Tests

Run all tests.

```bash
pytest
```

Run API tests.

```bash
pytest tests/test_api.py
```

Run CLI tests.

```bash
pytest tests/test_cli.py
```

Run External API tests.

```bash
pytest tests/test_external_api.py
```

---

# CLI Usage

Start the CLI.

```bash
python cli.py
```

Available options include:

- View Inventory
- Add Item
- Update Item
- Delete Item
- Search Product
- Import Product
- Exit

---

# Frontend Features

- Responsive inventory dashboard
- Add inventory items
- Update product information
- Delete inventory items
- Search OpenFoodFacts by barcode
- Import products directly into inventory
- Automatic inventory refresh

---

# External API

This project uses the **OpenFoodFacts API** to retrieve product information.

Example barcode:

```
737628064502
```

Returned information includes:

- Product Name
- Brand
- Category
- Ingredients
- Product Image

---
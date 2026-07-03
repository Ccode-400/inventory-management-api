import { useState } from "react";
import api from "../services/api";

function AddItem({ refresh }) {
  const [formData, setFormData] = useState({
    barcode: "",
    product_name: "",
    brand: "",
    price: "",
    stock: "",
    category: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/inventory", {
        ...formData,
        price: parseFloat(formData.price),
        stock: parseInt(formData.stock),
      });
      alert("Item added successfully!");
      setFormData({
        barcode: "",
        product_name: "",
        brand: "",
        price: "",
        stock: "",
        category: "",
      });
      refresh();
    } catch (error) {
      console.error(error);
      alert("Failed to add item.");
    }
  };

  return (
    <div className="form-container">
      <h2>Add New Item</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="barcode"
          placeholder="Barcode"
          value={formData.barcode}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="product_name"
          placeholder="Product Name"
          value={formData.product_name}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="brand"
          placeholder="Brand"
          value={formData.brand}
          onChange={handleChange}
          required
        />

        <input
          type="number"
          step="0.01"
          name="price"
          placeholder="Price"
          value={formData.price}
          onChange={handleChange}
          required
        />

        <input
          type="number"
          name="stock"
          placeholder="Stock"
          value={formData.stock}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="category"
          placeholder="Category"
          value={formData.category}
          onChange={handleChange}
          required
        />
        <button type="submit">
          Add Item
        </button>
      </form>
    </div>
  );
}

export default AddItem;
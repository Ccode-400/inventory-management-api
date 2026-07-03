import { useState, useEffect } from "react";
import api from "../services/api";

function UpdateItem({ item, refresh, onClose }) {
  const [formData, setFormData] = useState({
    price: "",
    stock: "",
    category: "",
  });

  useEffect(() => {
    if (item) {
      setFormData({
        price: item.price,
        stock: item.stock,
        category: item.category,
      });
    }
  }, [item]);
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.patch(`/inventory/${item.id}`, {
        price: parseFloat(formData.price),
        stock: parseInt(formData.stock),
        category: formData.category,
      });
      alert("Item updated successfully!");
      refresh();
      onClose();
    } catch (error) {
      console.error(error);
      alert("Failed to update item.");
    }
  };

  return (
    <div className="update-container">
      <h2>Edit Item</h2>
      <form onSubmit={handleSubmit}>
        <label>Price</label>
        <input
          type="number"
          step="0.01"
          name="price"
          value={formData.price}
          onChange={handleChange}
          required
        />

        <label>Stock</label>

        <input
          type="number"
          name="stock"
          value={formData.stock}
          onChange={handleChange}
          required
        />

        <label>Category</label>

        <input
          type="text"
          name="category"
          value={formData.category}
          onChange={handleChange}
          required
        />

        <div className="button-group">
          <button type="submit">
            Save Changes
          </button>
          <button
            type="button"
            onClick={onClose}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

export default UpdateItem;
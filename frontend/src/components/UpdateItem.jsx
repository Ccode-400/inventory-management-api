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
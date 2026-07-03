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
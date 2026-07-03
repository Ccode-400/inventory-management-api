import { useState } from "react";
import api from "../services/api";

function SearchProduct({ refresh }) {
  const [barcode, setBarcode] = useState("");
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(false);
  const searchProduct = async () => {
    if (!barcode.trim()) {
      alert("Please enter a barcode.");
      return;
    }
    setLoading(true);
    try {
      const response = await api.get(`/search/${barcode}`);
      setProduct(response.data);
    } catch (error) {
      console.error(error);
      alert("Product not found.");
      setProduct(null);
    }
    setLoading(false);
  };
  const importProduct = async () => {
    try {
      await api.post(`/import/${barcode}`);
      alert("Product imported successfully!");
      setBarcode("");
      setProduct(null);
      refresh();
    } catch (error) {
      console.error(error);
      alert("Failed to import product.");
    }
  };
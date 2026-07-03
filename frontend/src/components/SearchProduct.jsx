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

  return (
    <div className="search-container">
      <h2>Search OpenFoodFacts</h2>
      <input
        type="text"
        placeholder="Enter Barcode"
        value={barcode}
        onChange={(e) => setBarcode(e.target.value)}
      />
      <button onClick={searchProduct}>
        Search
      </button>
      {loading && <p>Searching...</p>}
      {product && (
        <div className="product-card">
          <h3>{product.product_name}</h3>
          <p>
            <strong>Brand:</strong> {product.brand}
          </p>
          <p>
            <strong>Category:</strong> {product.category}
          </p>
          <p>
            <strong>Ingredients:</strong>
            <br />
            {product.ingredients}
          </p>
          {product.image && (
            <img
              src={product.image}
              alt={product.product_name}
              width="180"
            />
          )}
          <br />
          <button onClick={importProduct}>
            Import Product
          </button>
        </div>
      )}
    </div>
  );
}

export default SearchProduct;
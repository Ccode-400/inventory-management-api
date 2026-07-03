import { useEffect, useState } from "react";
import api from "./services/api";
import InventoryList from "./components/InventoryList";
import AddItem from "./components/AddItem";
import SearchProduct from "./components/SearchProduct";
import "./App.css";

function App() {
  const [inventory, setInventory] = useState([]);
  const loadInventory = async () => {
    try {
      const response = await api.get("/inventory");
      setInventory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadInventory();
  }, []);

  return (
    <div className="container">
      <h1>Inventory Management System</h1>
      <AddItem refresh={loadInventory} />
      <SearchProduct refresh={loadInventory} />
      <InventoryList
        inventory={inventory}
        refresh={loadInventory}
      />
    </div>
  );
}

export default App;
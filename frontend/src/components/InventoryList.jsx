import api from "../services/api";
import { useState } from "react";
import UpdateItem from "./UpdateItem";

function InventoryList({ inventory, refresh }) {
    const [editingItem, setEditingItem] = useState(null);

    const deleteItem = async (id) => {
        const confirmDelete = window.confirm(
            "Are you sure you want to delete this item?"
        );

        if (!confirmDelete) return;
        try {
            await api.delete(`/inventory/${id}`);
            alert("Item deleted successfully!");
            refresh();
        } catch (error) {
            console.error(error);
            alert("Failed to delete item.");
        }
    };

    return (
        <div className="inventory-container">
            <h2>Inventory</h2>
            {selectedItem && (
                <UpdateItem
                    item={selectedItem}
                    refresh={refresh}
                    onClose={() => setSelectedItem(null)}
                />
            )}
            {inventory.length === 0 ? (
                <p>No inventory items found.</p>
            ) : (
                inventory.map((item) => (
                    <div
                        className="inventory-card"
                        key={item.id}
                    >
                        <h3>{item.product_name}</h3>
                        <p>
                            <strong>Brand:</strong> {item.brand}
                        </p>
                        <p>
                            <strong>Category:</strong> {item.category}
                        </p>
                        <p>
                            <strong>Price:</strong> ${item.price}
                        </p>
                        <p>
                            <strong>Stock:</strong> {item.stock}
                        </p>
                        <p>
                            <strong>Barcode:</strong> {item.barcode}
                        </p>
                        <div className="button-group">

                        <button
                            onClick={() => setSelectedItem(item)}
                        >
                            Edit
                            </button>

                        <button
                            className="delete-btn"
                            onClick={() => deleteItem(item.id)}
                        >
                            Delete
                            </button>
                            </div>
                        </div>
                     ))
                 )}
            </div>
        );
    }

export default InventoryList;
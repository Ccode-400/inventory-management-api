import api from "../services/api";

function InventoryList({ inventory, refresh }) {
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
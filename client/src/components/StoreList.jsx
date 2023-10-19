import React from "react";
import { Link } from "react-router-dom";

function StoreList({ addToCart}) {
  const items = [
    { id: 1, name: "Item 1", price: 10.99 },
    { id: 2, name: "Item 2", price: 15.99 },
    { id: 3, name: "Item 3", price: 8.99 },
  ];

  return (
    <div>
      <h1>Store List</h1>
      <Link to="/shopping-cart">
        <button>View Cart</button>
      </Link>
      <div>
        <h2>Items Available:</h2>
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              {item.name} - ${item.price}
              <button onClick={() => addToCart(item)}>Select</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default StoreList;

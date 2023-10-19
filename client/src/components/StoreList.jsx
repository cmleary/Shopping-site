import React from "react";
import { Link } from "react-router-dom";

function StoreList({ addToCart, allprod}) {
  

  return (
    <div>
      <h1>Store List</h1>
      <Link to="/shopping-cart">
        <button>View Cart</button>
      </Link>
      <div>
        <h2>Items Available:</h2>
        <ul>
          {allprod.map((item) => (
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

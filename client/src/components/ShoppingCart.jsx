import React from "react";

function ShoppingCart({ cart, onRemoveItem }) {
  return (
    <div>
      <h1>Shopping Cart</h1>
      <div>
        <h2>Shopping Cart:</h2>
        <ul>
          {cart.map((cartItem) => (
            <li key={cartItem.id}>
              {cartItem.name} - ${cartItem.price}
              <button onClick={() => onRemoveItem(cartItem.id)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ShoppingCart;

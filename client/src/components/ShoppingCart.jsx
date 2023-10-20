import React from "react";

function ShoppingCart({ cart, onRemoveItem, setCurrentUser }) {

  

  function order(cart) {
    fetch("/orders", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Accepts: "application/json",
        },
        body: JSON.stringify(cart),
    })
        .then((res) => res.json())
        .then((data) => setCurrentUser(data));
}


 
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
        <button onClick={() => order(cart)}>Order</button>
      </div>
    </div>
  );
}

export default ShoppingCart;

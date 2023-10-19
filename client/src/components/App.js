import React, { useEffect, useState } from "react";
import { Route, Routes, Link } from "react-router-dom";
import { BrowserRouter } from "react-router-dom";
import LogIn from "./Login";
import ShoppingCart from "./ShoppingCart";
import StoreList from "./StoreList";
import Signup from "./Signup";

function App() {
  const [cart, setCart] = useState([]);
  const [allprod, setAllprod] = useState([]);

  useEffect (() => {
    fetch('/products')
    .then(res => res.json())
    .then(carsData => setAllprod(carsData))
  },[])

  function addToCart(item) {
    setCart((prevCart) => [...prevCart, item]);
  }

  const removeItemFromCart = (itemId) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== itemId));
  }

  return (
    <div>
      <BrowserRouter>
        <nav>
          <ul>
            <li>
              <Link to="/">Log In</Link>
            </li>
            <li>
              <Link to="/signup">Sign Up</Link>
            </li>
            <li>
              <Link to="/shopping-cart">Shopping Cart</Link>
            </li>
            <li>
              <Link to="/store-list">Store List</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<LogIn  />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/shopping-cart" element={<ShoppingCart cart={cart} onRemoveItem={removeItemFromCart} />} />
          <Route path="/store-list" element={<StoreList cart={cart} addToCart={addToCart} allprod={allprod}/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

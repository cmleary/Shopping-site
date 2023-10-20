import React, { useEffect, useState } from "react";
import { Route, Link } from "react-router-dom";
import { BrowserRouter } from "react-router-dom";
import LogIn from "./Login";
import ShoppingCart from "./ShoppingCart";
import StoreList from "./StoreList";
import Signup from "./Signup";
import { Switch } from "react-router-dom/cjs/react-router-dom.min";
import NavBar from "./NavBar";

function App() {
  const [cart, setCart] = useState([]);
  const [allprod, setAllprod] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((res) => {
        if (res.ok) {
            res.json().then((user) => setCurrentUser(user));
        }
    });
}, []);

  useEffect(() => {
    fetch("/check_session").then((res) => {
        if (res.ok) {res.json().then(() => setCart([]));
      } 
    });
}, [currentUser]);


  function attemptSignup(userInfo) {
      fetch("/users", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              Accepts: "application/json",
          },
          body: JSON.stringify(userInfo),
      })
          .then((res) => res.json())
          .then((data) => setCurrentUser(data));
  }

  function attemptLogin(userInfo) {
      fetch("/login", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              Accepts: "application/json",
          },
          body: JSON.stringify(userInfo),
      })
          .then((res) => res.json())
          .then((data) => setCurrentUser(data));
  }

  function logout() {
      fetch("/logout", { method: "DELETE" }).then((res) => {
          if (res.ok) {
              setCurrentUser(null);
          }
      });
  }

  useEffect (() => {
    fetch('/products')
    .then(res => res.json())
    .then(carsData =>{ console.log(carsData);setAllprod(carsData)})
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
              {currentUser ?  <Link to="/shopping-cart">{currentUser.username}'s Shopping Cart</Link> : null}
            </li>
            <li>
              <Link to="/store-list">Store List</Link>
            </li>
            <button onClick={logout}>Logout</button>
          </ul>
        </nav>

        <Switch>
          <Route path="/signup"><Signup attemptSignup={attemptSignup} /></Route>
          <Route path="/shopping-cart"><ShoppingCart cart={cart} onRemoveItem={removeItemFromCart} setCurrentUser = {setCurrentUser} /></Route>
          <Route path="/store-list"><StoreList cart={cart} addToCart={addToCart} allprod={allprod}/></Route>
          <Route path="/"><LogIn attemptLogin={attemptLogin} /></Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;

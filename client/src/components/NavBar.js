import React from "react";
import { NavLink } from "react-router-dom";

function NavBar() {
    
    
    return (
        <nav>
            <NavLink to="/">Log In</NavLink>
            <NavLink to="/signup">Sign Up</NavLink>
            <NavLink to="/shopping-cart">Shopping Cart</NavLink>
            <NavLink to="/store-list">Store List</NavLink>
        </nav>
    );
}

export default NavBar;
import React, { useState } from "react";

function Signup({ attemptSignup }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleChangeUsername = (e) => setUsername(e.target.value);
    const handleChangePassword = (e) => setPassword(e.target.value);

    function handleSubmit(e) {
        e.preventDefault();

        const user = { username, password };

        fetch("/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        })
            .then((response) => response.json())
            .then((data) => {
                attemptSignup(data);
            })
            .catch((error) => {
                console.error("Error signing up:", error);
            });
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>Signup</h2>

            <input
                type="text"
                onChange={handleChangeUsername}
                value={username}
                placeholder="username"
            />

            <input
                type="password"
                onChange={handleChangePassword}
                value={password}
                placeholder="password"
            />

            <input type="submit" value="Signup" />
        </form>
    );
}

export default Signup;

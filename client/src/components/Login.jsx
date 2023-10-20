import React, { useState } from "react";

function Login({ attemptLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleChangeUsername = (e) => setUsername(e.target.value);
    const handleChangePassword = (e) => setPassword(e.target.value);

    function handleSubmit(e) {
        e.preventDefault();
        attemptLogin({ username, password });

        // const user = { username, password };

        // fetch("/login", {
        //     method: "POST",
        //     headers: {
        //         "Content-Type": "application/json",
        //     },
        //     body: JSON.stringify(user),
        // })
        //     .then((response) => response.json())
        //     .then((data) => {attemptLogin(data);
        //     })
        //     .catch((error) => {
        //         console.error("Error logging in:", error);
        //     });
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h2>Login</h2>

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

                <input type="submit" value="Login" />
            </form>
        </div>
    );
}

export default Login;

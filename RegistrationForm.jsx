import { useState } from "react";

export default function RegistrationForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({ username: "", password: "" });

  
  const validateUsername = (value) => {
    setErrors((prev) => ({
      ...prev,
      username: value.length < 3 ? "Username must be at least 3 characters long" : "",
    }));
  };

  const validatePassword = (value) => {
    setErrors((prev) => ({
      ...prev,
      password: value.length < 8 ? "Password must be at least 8 characters long" : "",
    }));
  };


  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
    validateUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    validatePassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`User Registered!\nUsername: ${username}\nPassword: ${password}`);
  };

  const isFormValid = username.length >= 3 && password.length >= 8;

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: "15px" }}>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={handleUsernameChange}
            style={{ display: "block", width: "100%", padding: "8px", marginTop: "5px" }}
          />
          {errors.username && <span style={{ color: "red" }}>{errors.username}</span>}
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
            style={{ display: "block", width: "100%", padding: "8px", marginTop: "5px" }}
          />
          {errors.password && <span style={{ color: "red" }}>{errors.password}</span>}
        </div>

        <button type="submit" disabled={!isFormValid} style={{ padding: "10px 20px" }}>
          Register
        </button>
      </form>
    </div>
  );
}

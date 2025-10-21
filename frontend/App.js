import React, { useState } from "react";
import "./style.css";

function App() {
  const [data, setData] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:5000/validate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ dataset: data }),
    });
    const result = await response.json();
    setMessage(result.message);
  };

  return (
    <div className="container">
      <h1>🗂️ Data Lighthouse</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Paste your dataset here..."
          value={data}
          onChange={(e) => setData(e.target.value)}
        />
        <button type="submit">Validate</button>
      </form>
      {message && <p className="result">{message}</p>}
    </div>
  );
}

export default App;

import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const [form, setForm] = useState({
    state: "",
    fuel: "",
    sector: "",
    tone: ""
  });

  console.log("NODE_ENV:", process.env.NODE_ENV);

  useEffect(() => {
    fetch("http://localhost:8000/api/hello")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  const handleChangeForm = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const query = new URLSearchParams(form).toString();

    fetch(`http://localhost:8000/api/echo?${query}`)
      .then((res) => res.json())
      .then((data) => setResponse(data.message));
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>{message}</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="state"
          placeholder="State"
          value={form.state}
          onChange={handleChangeForm}
          style={{ marginBottom: "0.5rem", display: "block" }}
        />
        <input
          type="text"
          name="fuel"
          placeholder="Fuel"
          value={form.fuel}
          onChange={handleChangeForm}
          style={{ marginBottom: "0.5rem", display: "block" }}
        />
        <input
          type="text"
          name="sector"
          placeholder="Sector"
          value={form.sector}
          onChange={handleChangeForm}
          style={{ marginBottom: "0.5rem", display: "block" }}
        />
        <input
          type="text"
          name="tone"
          placeholder="Tone"
          value={form.tone}
          onChange={handleChangeForm}
          style={{ marginBottom: "1rem", display: "block" }}
        />
        <button type="submit">Send</button>
      </form>

      <p style={{ marginTop: "1rem" }}>
        {response}
      </p>
    </div>
  );
}

export default App;

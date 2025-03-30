import { useState } from "react";

function App() {
  const [response, setResponse] = useState("");

  const [form, setForm] = useState({
    state: "",
    fuel: "",
    sector: "",
    tone: ""
  });

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
      <h1>Welcome to my CO2 Emission Summarizer!</h1>

      <p>This app will retrieve historical CO2 emission data provided by the U.S. Energy Information Administration, then send it to Claude AI to summarize for you.</p>
      <p>You have a few options for what data to retrieve:</p>
      <p>state: The name of the US state you'd like to see</p>
      <p>fuel: The type of fuel you'd like to see - leaving this empty will return the total of all fuels</p>
      <p>sector: The sector you'd like to see (e.g. residential, industrial)</p>
      <p>tone: The tone you would like Claude to respond in. Please use an adverb (e.g. professionally, sarcastically)</p>

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

import { useState } from "react";

function App() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

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

    if (loading) return; // Prevent if already in-flight
    setLoading(true);

    const query = new URLSearchParams(form).toString();

    fetch(`http://localhost:8000/api/retrieve?${query}`)
      .then((res) => res.json())
      .then((data) => setResponse(data.message))
      .catch((err) => {
        console.error("Request failed:", err);
        setResponse("Error: Something went wrong.");
      })
      .finally(() => setLoading(false));
  };

  const US_STATES = [
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
  ];

  const FUEL_OPTIONS = {
    CO: "Coal",
    NG: "Natural Gas",
    PE: "Petroleum",
    TO: "All Fuel"
  };

  const SECTOR_OPTIONS = {
    CC: "commercial",
    IC: "industrial",
    TC: "transportation",
    EC: "electric power",
    RC: "residential"
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Welcome to my CO2 Emission Summarizer!</h1>

      <p>This app will retrieve historical CO2 emission data provided by the U.S. Energy Information Administration, then send it to Claude AI to summarize for you.</p>
      <p>You have a few options for what data to retrieve:</p>
      <p>state: The name of the US state you'd like to see</p>
      <p>fuel: The type of fuel you'd like to see - leaving this empty will return the total of all fuels</p>
      <p>sector: The sector you'd like to see (e.g. residential, industrial)</p>
      <p>tone: The tone you would like Claude to respond in. Please use an adverb (e.g. professionally, sarcastically, "like a southern belle")</p>

      <form onSubmit={handleSubmit}>
        <label style={{ display: "block", marginBottom: "0.5rem" }}>
          State:
          <select
            name="state"
            value={form.state}
            onChange={handleChangeForm}
            style={{ marginLeft: "0.5rem" }}
          >
            <option value="">-- Select State --</option>
            {US_STATES.map((abbr) => (
              <option key={abbr} value={abbr}>
                {abbr}
              </option>
            ))}
          </select>
        </label>
        <label style={{ display: "block", marginBottom: "0.5rem" }}>
          Fuel:
          <select
            name="fuel"
            value={form.fuel}
            onChange={handleChangeForm}
            style={{ marginLeft: "0.5rem" }}
          >
            <option value="">-- Select Fuel --</option>
            {Object.entries(FUEL_OPTIONS).map(([code, label]) => (
              <option key={code} value={code}>
                {label}
              </option>
            ))}
          </select>
        </label>
        <label style={{ display: "block", marginBottom: "0.5rem" }}>
          Sector:
          <select
            name="sector"
            value={form.sector}
            onChange={handleChangeForm}
            style={{ marginLeft: "0.5rem" }}
          >
            <option value="">-- Select Sector --</option>
            {Object.entries(SECTOR_OPTIONS).map(([code, label]) => (
              <option key={code} value={code}>
                {label}
              </option>
            ))}
          </select>
        </label>
        <input
          type="text"
          name="tone"
          placeholder="Tone"
          value={form.tone}
          onChange={handleChangeForm}
          style={{ marginBottom: "1rem", display: "block" }}
        />
        <button type="submit">Submit</button>
      </form>

      <p style={{ marginTop: "1rem", whiteSpace: "pre-wrap" }}>
        {response}
      </p>
    </div>
  );
}

export default App;

import { useState } from "react";
import InputForm from "./InputForm";
import DataTable from "./DataTable";
import Conversation from "./Conversation";

function App() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [tableData, setTableData] = useState([]);
  const [messages, setMessages] = useState([]);

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

    if (loading) return;
    setLoading(true);

    const query = new URLSearchParams({
      state: form.state,
      fuel: form.fuel,
      sector: form.sector,
      tone: form.tone || "professionally",
      messages: JSON.stringify(messages),
    }).toString();
    
    fetch(`http://localhost:8000/api/retrieve?${query}`)
      .then((res) => res.json())
      .then((data) => {
        setResponse(data.message);
        setMessages(data.conversation || []);

        const sortedTable = [...(data.data || [])].sort(
          (a, b) => Number(b.period) - Number(a.period)
        );
        setTableData(sortedTable);
      })
      .catch((err) => {
        console.error("Request failed:", err);
        setResponse("Error: Something went wrong.");
      })
      .finally(() => setLoading(false));

  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Welcome to My CO2 Emission Summarizer!</h1>

      <p>This app will retrieve historical CO2 emission data provided by the U.S. Energy Information Administration, then send it to Claude AI to summarize for you.</p>
      <p>You have a few options for what data to retrieve:</p>
      <p>state: The name of the US state you'd like to see</p>
      <p>fuel: The type of fuel you'd like to see - leaving this empty will return the total of all fuels</p>
      <p>sector: The sector you'd like to see (e.g. residential, industrial)</p>
      <p>tone: The tone you would like Claude to respond in. Please use an adverb (e.g. professionally, sarcastically, "like a southern belle")</p>

      <InputForm
        form={form}
        onChange={handleChangeForm}
        onSubmit={handleSubmit}
        loading={loading}
      />

      {response && (<h1 style={{ marginTop: "1rem", whiteSpace: "pre-wrap" }}>
        {response}
      </h1>)}
      
      <DataTable
        data={tableData}
      />

      <Conversation
        messages={messages}
      />
    </div>
  );
}

export default App;

export default function Conversation({ messages }) {
    if (!messages || messages.length === 0) return null;
  
    return ((
        <div style={{ marginTop: "2rem" }}>
          <h2>🗣️ Conversation History</h2>
          <div style={{ border: "1px solid #ccc", padding: "1rem", borderRadius: "8px" }}>
            {messages.map((msg, idx) => (
              <div
                key={idx}
                style={{
                  marginBottom: "1rem",
                  background: msg.role === "assistant" ? "#f0f8ff" : "#fff",
                  padding: "0.75rem",
                  borderRadius: "6px"
                }}
              >
                <strong>{msg.role === "assistant" ? "Claude" : "You"}:</strong>
                <p style={{ whiteSpace: "pre-wrap", marginTop: "0.5rem" }}>
                  {msg.content}
                </p>
              </div>
            ))}
          </div>
        </div>
      ));
}
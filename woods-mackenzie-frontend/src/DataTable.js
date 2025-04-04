import React from "react";

const thStyle = {
  border: "1px solid #ccc",
  padding: "0.5rem",
  backgroundColor: "#f4f4f4",
  textAlign: "left"
};

const tdStyle = {
  border: "1px solid #ccc",
  padding: "0.5rem"
};

export default function DataTable({ data }) {
  if (!data || data.length === 0) return null;

  const sorted = [...data].sort((a, b) => b.period - a.period);

  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>📊 Emissions Data Table</h2>
      <table style={{ borderCollapse: "collapse", width: "100%", marginTop: "1rem" }}>
        <thead>
          <tr>
            <th style={thStyle}>Year</th>
            <th style={thStyle}>State</th>
            <th style={thStyle}>Economic Sector</th>
            <th style={thStyle}>CO₂ Emissions</th>
            <th style={thStyle}>Units</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((row) => (
            <tr key={row.period}>
              <td style={tdStyle}>{row.period}</td>
              <td style={tdStyle}>{row["state-name"]}</td>
              <td style={tdStyle}>{row["sector-name"]}</td>
              <td style={tdStyle}>{parseFloat(row.value).toFixed(3)}</td>
              <td style={tdStyle}>{row["value-units"]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

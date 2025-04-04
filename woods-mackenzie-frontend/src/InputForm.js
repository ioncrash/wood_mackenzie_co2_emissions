import React from "react";

const US_STATES = [
  "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
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

export default function InputForm({ form, onChange, onSubmit, loading }) {
  return (
    <form onSubmit={onSubmit}>
      <label style={{ display: "block", marginBottom: "0.5rem" }}>
        State:
        <select
          name="state"
          value={form.state}
          onChange={onChange}
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
          onChange={onChange}
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
          onChange={onChange}
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
        onChange={onChange}
        style={{ marginBottom: "1rem", display: "block" }}
      />

      <button type="submit" disabled={loading}>
        {loading ? "Loading..." : "Submit"}
      </button>
    </form>
  );
}

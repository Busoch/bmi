import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api";
import LogoutButton from "./LogoutButton";

export default function BMICalculator() {
  const [form, setForm] = useState({ weight: "", height: "" });
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await API.post("bmi/", form);
      setResult(res.data);

      // ✅ Clear input fields after success
      setForm({ weight: "", height: "" });
    } catch (err) {
      setError("Failed to calculate BMI. Please try again.");
    }
  };

  return (
    <div>
      {/* ✅ Top-right button group */}
      <div className="top-buttons">
        <button className="history-btn" onClick={() => navigate("/history")}>
          History
        </button>
        <LogoutButton />
      </div>

      <div className="container">
        <h2>BMI Calculator</h2>
        <form onSubmit={handleSubmit}>
          <input
            name="weight"
            type="number"
            placeholder="Weight (kg)"
            value={form.weight}
            onChange={handleChange}
            required
          />
          <input
            name="height"
            type="number"
            placeholder="Height (cm)"
            value={form.height}
            onChange={handleChange}
            required
          />
          <button type="submit">Calculate</button>
        </form>

        {error && <p className="error">{error}</p>}

        {result && (
          <div className="result">
            <p>Your BMI: {result.bmi}</p>
            <p>Category: {result.category}</p>
          </div>
        )}
      </div>
    </div>
  );
}

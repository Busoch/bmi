import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import BMICalculator from "./pages/BMICalculator";
import History from "./pages/History";

function App() {
  return (
    <Router>
      <Routes>
        {/* ✅ Redirect root (/) to /login */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/bmi" element={<BMICalculator />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </Router>
  );
}

export default App;

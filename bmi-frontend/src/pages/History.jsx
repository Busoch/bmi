import { useEffect, useState } from "react";
import API from "../api";

export default function History() {
  const [records, setRecords] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const recordsPerPage = 10;

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const res = await API.get("bmi/history/");
        setRecords(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchHistory();
  }, []);

  // ✅ Pagination logic
  const indexOfLastRecord = currentPage * recordsPerPage;
  const indexOfFirstRecord = indexOfLastRecord - recordsPerPage;
  const currentRecords = records.slice(indexOfFirstRecord, indexOfLastRecord);
  const totalPages = Math.ceil(records.length / recordsPerPage);

  return (
    <div className="history-container">
      <h2 className="history-title">BMI History</h2>
      <ul className="history-list">
        {currentRecords.map((rec) => (
          <li key={rec.id} className="history-item">
            <span className="history-date">{rec.created_at}</span>
            <span className="history-details">
              BMI {rec.bmi} ({rec.category}) – {rec.weight}kg, {rec.height}cm
            </span>
          </li>
        ))}
      </ul>

      {/* ✅ Pagination controls */}
      {totalPages > 1 && (
        <div className="pagination">
          <button
            disabled={currentPage === 1}
            onClick={() => setCurrentPage((p) => p - 1)}
          >
            Prev
          </button>
          <span>
            Page {currentPage} of {totalPages}
          </span>
          <button
            disabled={currentPage === totalPages}
            onClick={() => setCurrentPage((p) => p + 1)}
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
}

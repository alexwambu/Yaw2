import { useState } from "react";

function App() {
  const [script, setScript] = useState("");
  const [status, setStatus] = useState("");

  const generateVideo = async () => {
    setStatus("Processing...");
    const res = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ script }),
    });
    const data = await res.json();
    setStatus("Done! File: " + data.file);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>🎬 AI Video Creator</h1>
      <textarea
        style={{ width: "100%", height: "150px", marginTop: "1rem" }}
        placeholder="Enter your movie script..."
        value={script}
        onChange={(e) => setScript(e.target.value)}
      />
      <br />
      <button
        style={{
          marginTop: "1rem",
          padding: "10px 20px",
          background: "blue",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
        onClick={generateVideo}
      >
        Generate Movie
      </button>
      <p style={{ marginTop: "1rem" }}>{status}</p>
    </div>
  );
}

export default App;

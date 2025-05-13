import React, { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const [advice, setAdvice] = useState("");
  const [responseType, setResponseType] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // LLM advice
    const llmRes = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: inputText }),
    });
    const llmData = await llmRes.json();
    setAdvice(llmData.advice);

    // ML prediction
    const mlRes = await fetch("http://localhost:8000/predict-response-type", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: inputText }),
    });
    const mlData = await mlRes.json();
    setResponseType(mlData.response_type);
  };

  return (
    <div className="p-4 max-w-xl mx-auto font-sans">
      <h1 className="text-3xl font-bold mb-6 text-blue-700">Counselor Assistant</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          className="w-full p-3 border rounded shadow"
          rows={4}
          placeholder="Describe your patient's challenge..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-5 py-2 rounded hover:bg-blue-700"
        >
          Submit
        </button>
      </form>

      {responseType && (
        <div className="mt-6 p-4 bg-blue-50 border-l-4 border-blue-400">
          <h2 className="font-semibold mb-1 text-blue-800">Predicted Response Type:</h2>
          <p className="text-blue-900">{responseType}</p>
        </div>
      )}

      {advice && (
        <div className="mt-4 p-4 bg-green-50 border-l-4 border-green-400">
          <h2 className="font-semibold mb-1 text-green-800">LLM Advice:</h2>
          <p className="text-green-900">{advice}</p>
        </div>
      )}
    </div>
  );
}

export default App;

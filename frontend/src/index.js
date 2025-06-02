import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

const App = () => {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState(null);
  const [file, setFile] = useState(null);

  const generateImage = async () => {
    const res = await fetch("http://localhost:8000/generate-image/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    setImage(data.image_url || null);
  };

  const handleUpload = (e) => {
    setFile(URL.createObjectURL(e.target.files[0]));
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Legenie AI Image Generator</h1>
      <input
        type="text"
        className="w-full p-2 border mb-3"
        placeholder="Enter a prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={generateImage}
      >
        Generate
      </button>

      {image && (
        <div className="mt-6">
          <h2 className="text-lg mb-2">Generated Image:</h2>
          <img src={image} alt="Generated" className="rounded" />
        </div>
      )}

      <div className="mt-6">
        <h2 className="text-lg mb-2">Upload Preview:</h2>
        <input type="file" onChange={handleUpload} />
        {file && <img src={file} alt="Preview" className="mt-3 rounded" />}
      </div>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

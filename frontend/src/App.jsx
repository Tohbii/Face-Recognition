import { useState } from "react";

import Header from "./components/Header";
import UploadForm from "./components/UploadForm";
import PredictionCard from "./components/PredictionCard";

function App() {

  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-[#080c14] text-white font-mono flex flex-col items-center justify-center px-4 py-12 relative overflow-hidden">


        {/* Grid background */}
      <div
        className="absolute inset-0 opacity-[0.04]"
        style={{
          backgroundImage:
            "linear-gradient(#00f5ff 1px, transparent 1px), linear-gradient(90deg, #00f5ff 1px, transparent 1px)",
          backgroundSize: "40px 40px",
        }} 
      />

      <Header />

      <div className="w-full max-w-4xl">

        <UploadForm setResult={setResult} />

        <PredictionCard result={result} />

      </div>

    </div>
  );
}

export default App;
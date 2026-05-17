import { useState, useRef } from "react";

import API from "../services/api";

import Loader from "./Loader";

function UploadForm({ setResult }) {

  

  const [image, setImage] = useState(null);

  const inputRef = useRef();

  const [preview, setPreview] = useState(null);

  const [isDragging, setIsDragging] = useState(false);

  const [loading, setLoading] = useState(false);

 

  const handleImageChange = (e) => {

    const file = e.target.files[0];

    setImage(file);

    setPreview(URL.createObjectURL(file));
  };


   const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const f = e.dataTransfer.files[0];
    if (f && f.type.startsWith("image/")) handleImageChange({ target: { files: [f] } });
  };


  const handleSubmit = async () => {

    if (!image) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();

    formData.append("image", image);

    try {

      setLoading(true);

      const response = await API.post(
        "/predict",
        formData
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Prediction failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="relative z-10 w-full max-w-md">


      <div className="border border-white/[0.07] bg-white/[0.03] backdrop-blur-sm rounded-2xl p-6 shadow-[0_0_60px_rgba(0,245,255,0.04)] ">

      <div
      onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={handleDrop}
            onClick={() => inputRef.current.click()}
            className={`relative cursor-pointer rounded-xl border-2 border-dashed transition-all duration-300 flex flex-col items-center justify-center text-center mb-4 overflow-hidden
              ${isDragging
                ? "border-cyan-400 bg-cyan-500/10"
                : preview
                ? "border-white/10 bg-transparent"
                : "border-white/10 hover:border-cyan-500/40 hover:bg-white/[0.02]"
              }
              ${preview ? "w-48" : "h-48"}
            `}
               >

          
          
            {preview ? (
              <>
                <img
                  src={preview}
                  alt="preview"
                  className="w-full h-full object-cover rounded-xl"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent rounded-xl" />
                <p className="absolute bottom-3 left-0 right-0 text-center text-xs text-cyan-300 tracking-widest uppercase">
                  {image?.name}
                </p>
                {/* Corner scan brackets */}
                <div className="absolute top-2 left-2 w-5 h-5 border-t-2 border-l-2 border-cyan-400 rounded-tl" />
                <div className="absolute top-2 right-2 w-5 h-5 border-t-2 border-r-2 border-cyan-400 rounded-tr" />
                <div className="absolute bottom-2 left-2 w-5 h-5 border-b-2 border-l-2 border-cyan-400 rounded-bl" />
                <div className="absolute bottom-2 right-2 w-5 h-5 border-b-2 border-r-2 border-cyan-400 rounded-br" />
              </>
            ) : (
              <div className="px-6 py-4">

                {/* upload button */}
                <div className="mx-auto mb-3 w-12 h-12 rounded-full border border-white/10 flex items-center justify-center bg-white/5">
                  <svg className="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
                  </svg>
                </div>
                <p className="text-slate-300 text-sm font-medium">Drop image here</p>
                <p className="text-slate-600 text-xs mt-1">or click to browse · JPG, PNG, WEBP</p>
              </div>
            )}
            <input
              ref={inputRef}
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => handleImageChange(e)}
            />

      </div>

     

      <button
        onClick={handleSubmit}
        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl"
      >
        Predict Face
      </button>

      {loading && <Loader />}
    </div>



    </div>
    
  );
}

export default UploadForm;
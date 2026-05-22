function Header() {
  return (
    
    <div className="relative z-10 text-center mb-10">
        <div className="inline-flex items-center gap-2 border border-cyan-500/30 bg-cyan-500/5 px-4 py-1.5 rounded-full text-cyan-400 text-xs tracking-widest uppercase mb-5">
          <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
          System Online · LBPH Engine v2.4
        </div>
        <h1 className="text-5xl font-black tracking-tight leading-none mb-2">
          <span className="text-white">FACIAL</span>
          <br />
          <span
            className="text-transparent bg-clip-text"
            style={{
              backgroundImage: "linear-gradient(90deg, #00f5ff, #3b82f6)",
            }}
          >
            RECOGNITION
          </span>
        </h1>
        <p className="text-slate-500 text-xs tracking-[0.2em] uppercase mt-3">
          React · Flask · OpenCV · LBPH
        </p>
      </div>
  );
}

export default Header;
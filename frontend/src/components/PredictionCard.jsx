function PredictionCard({ result }) {

  if (!result) return null;

  return (
    <div className="mt-4 border border-cyan-500/20 bg-cyan-500/5 rounded-xl p-4">

      <div className="flex items-center justify-between mb-3" >

        <h2 className="text-2xl font-bold  uppercase tracking-widest mb-3">
        Prediction Result
        </h2>

      </div>

      

      <div className="space-y-3">

        <div className="text-xl font-black text-cyan-300 tracking-wider mb-2"> 
          <span className="font-semibold">
            Status:
          </span>

          {" "}
          {result.status}
        </div>

        <div>
          <span className="font-semibold">
            Predicted Person:
          </span>

          {" "}
          {result.predicted_person}
        </div>

        <div>
          <span className="font-semibold">
            Confidence:
          </span>

          {" "}
          {result.confidence}
        </div>

        {result.message && (
          <div className="text-red-500">
            {result.message}
          </div>
        )}

      </div>
    </div>
  );
}

export default PredictionCard;
function PredictionCard({ result }) {

  if (!result) return null;

  return (
    <div className="bg-white rounded-2xl shadow-2xl p-6 mt-8">

      <h2 className="text-2xl font-bold mb-4">
        Prediction Result
      </h2>

      <div className="space-y-3">

        <div>
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
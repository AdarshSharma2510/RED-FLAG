import Button from "../common/Button";

import EmptyResults from "./EmptyResults";
import ResultCard from "./ResultCard";

const severityOrder = {
  HIGH: 3,
  MEDIUM: 2,
  LOW: 1,
};

export default function ResultsScreen({
  result,
  onAnalyzeAnother,
}) {
  const { document, results } = result;

  const sortedResults = [...results].sort(
    (a, b) =>
      severityOrder[b.finding.severity] -
      severityOrder[a.finding.severity]
  );

  const highestSeverity =
    sortedResults.length > 0
      ? sortedResults[0].finding.severity
      : "None";

  return (
    <div className="space-y-8">

      {/* Summary Card */}

      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

        <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">

          <div>

            <h1 className="text-3xl font-bold text-slate-900">
              Analysis Complete
            </h1>

            <p className="mt-2 text-slate-600">
              Your contract has been successfully analyzed.
            </p>

          </div>

          <Button onClick={onAnalyzeAnother}>
            Analyze Another Contract
          </Button>

        </div>

        <div className="mt-8 grid gap-4 md:grid-cols-3">

          <div className="rounded-2xl bg-slate-50 p-5">
            <p className="text-sm text-slate-500">
              Contract
            </p>

            <p className="mt-1 font-semibold text-slate-900 break-all">
              {document.filename}
            </p>
          </div>

          <div className="rounded-2xl bg-slate-50 p-5">
            <p className="text-sm text-slate-500">
              Risks Found
            </p>

            <p className="mt-1 text-3xl font-bold text-slate-900">
              {results.length}
            </p>
          </div>

          <div className="rounded-2xl bg-slate-50 p-5">
            <p className="text-sm text-slate-500">
              Highest Severity
            </p>

            <p className="mt-1 text-xl font-bold text-red-700">
              {highestSeverity}
            </p>
          </div>

        </div>

      </div>

      {/* Results */}

      {results.length === 0 ? (
        <EmptyResults />
      ) : (
        <div className="space-y-6">

          {sortedResults.map((item, index) => (
            <ResultCard
              key={`${item.finding.clause_id}-${item.finding.sentence_id}-${index}`}
              result={item}
            />
          ))}

        </div>
      )}

    </div>
  );
}
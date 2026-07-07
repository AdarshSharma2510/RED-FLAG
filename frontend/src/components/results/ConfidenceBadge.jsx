export default function ConfidenceBadge({ confidence }) {
  return (
    <div className="rounded-xl bg-slate-50 px-4 py-2 text-right">
      <p className="text-xs uppercase tracking-wide text-slate-500">
        Confidence
      </p>

      <p className="text-lg font-bold text-slate-900">
        {Math.round(confidence * 100)}%
      </p>
    </div>
  );
}
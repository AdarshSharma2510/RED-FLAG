const severityStyles = {
  HIGH: "bg-red-100 text-red-700 border-red-200",
  MEDIUM: "bg-amber-100 text-amber-700 border-amber-200",
  LOW: "bg-green-100 text-green-700 border-green-200",
};

export default function SeverityBadge({ severity }) {
  return (
    <span
      className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-semibold ${
        severityStyles[severity] ??
        "bg-slate-100 text-slate-700 border-slate-200"
      }`}
    >
      {severity}
    </span>
  );
}
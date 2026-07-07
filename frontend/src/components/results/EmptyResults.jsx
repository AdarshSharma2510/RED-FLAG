import { ShieldCheck } from "lucide-react";

export default function EmptyResults() {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-12 text-center shadow-sm">
      <ShieldCheck
        className="mx-auto mb-5 text-green-600"
        size={48}
      />

      <h2 className="text-2xl font-bold text-slate-900">
        No Risks Detected
      </h2>

      <p className="mt-4 text-slate-600">
        No rule-based legal risks were detected.
      </p>

      <p className="mt-2 text-sm text-slate-500">
        This does not constitute legal advice.
      </p>
    </div>
  );
}
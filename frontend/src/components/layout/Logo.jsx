import { ShieldAlert } from "lucide-react";

/**
 * Application branding component.
 */
export default function Logo() {
  return (
    <div className="flex items-center gap-3">
      <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-red-700 text-white shadow-sm">
        <ShieldAlert size={24} strokeWidth={2.2} />
      </div>

      <div>
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">
          RED FLAG
        </h1>

        <p className="text-sm text-slate-500">
          AI Legal Contract Risk Analyzer
        </p>
      </div>
    </div>
  );
}
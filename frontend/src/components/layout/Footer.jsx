import { Scale } from "lucide-react";

export default function Footer() {
  return (
    <footer className="mt-12 border-t border-slate-200 py-6">
      <div className="mx-auto flex max-w-6xl items-start justify-center gap-3 px-6 text-center text-sm text-slate-500">
        <Scale
          size={18}
          className="mt-0.5 flex-shrink-0 text-red-600"
        />

        <p>
          <span className="font-semibold text-slate-700">
            Disclaimer:
          </span>{" "}
          RED FLAG is an AI-assisted educational project and does not
          provide legal advice. The analysis may be incomplete or
          inaccurate. Always consult a qualified legal professional
          before making legal or contractual decisions.
        </p>
      </div>
    </footer>
  );
}
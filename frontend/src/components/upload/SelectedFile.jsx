import {
  FileText,
  RefreshCw,
  X,
} from "lucide-react";

export default function SelectedFile({
  file,
  onReplace,
  onRemove,
}) {
  const size = (file.size / (1024 * 1024)).toFixed(2);

  return (
    <div className="mt-6 rounded-2xl border border-slate-200 bg-slate-50 p-5">
      <div className="flex flex-col gap-5 md:flex-row md:items-center md:justify-between">
        <div className="flex items-center gap-4">
          <div className="rounded-xl bg-red-100 p-3 text-red-700">
            <FileText size={22} />
          </div>

          <div>
            <p className="font-medium text-slate-900">
              {file.name}
            </p>

            <p className="text-sm text-slate-500">
              {size} MB
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={onReplace}
            className="inline-flex items-center gap-2 rounded-xl border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-100"
          >
            <RefreshCw size={16} />
            Replace File
          </button>

          <button
            type="button"
            onClick={onRemove}
            className="rounded-xl border border-slate-300 p-2 text-slate-600 transition hover:bg-slate-100 hover:text-red-700"
            aria-label="Remove file"
          >
            <X size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}
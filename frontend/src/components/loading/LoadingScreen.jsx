import { LoaderCircle } from "lucide-react";
import { useEffect, useState } from "react";

const loadingMessages = [
  "Uploading contract...",
  "Extracting text...",
  "Detecting clauses...",
  "Running legal analysis...",
  "Evaluating risks...",
  "Finalizing report...",
];

export default function LoadingScreen() {
  const [messageIndex, setMessageIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setMessageIndex((prev) =>
        Math.min(prev + 1, loadingMessages.length - 1)
        );
    }, 3500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-1 items-center justify-center">
      <div className="w-full max-w-xl rounded-3xl border border-slate-200 bg-white p-12 text-center shadow-sm">
        <LoaderCircle
          size={52}
          className="mx-auto animate-spin text-red-700"
        />

        <h2 className="mt-8 text-2xl font-bold text-slate-900">
          Analyzing Contract
        </h2>

        <p className="mt-6 text-lg text-slate-600 transition-all duration-300">
          {loadingMessages[messageIndex]}
        </p>

        <p className="mt-10 text-sm text-slate-400">
          This may take a few seconds depending on the size of your document.
        </p>
      </div>
    </div>
  );
}
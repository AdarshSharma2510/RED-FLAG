import { useCallback } from "react";
import { UploadCloud } from "lucide-react";
import { useDropzone } from "react-dropzone";

import { MAX_FILE_SIZE } from "../../utils/constants";

export default function UploadZone({
  onFileSelect,
  onBrowse,
}) {
  const onDrop = useCallback(
    (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        onFileSelect(acceptedFiles[0]);
      }
    },
    [onFileSelect]
  );

  const { getRootProps, getInputProps, isDragActive } =
    useDropzone({
      onDrop,
      multiple: false,
      noClick: true,
      accept: {
        "application/pdf": [".pdf"],
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
          [".docx"],
        "text/plain": [".txt"],
      },
      maxSize: MAX_FILE_SIZE,
    });

  return (
    <section
      {...getRootProps()}
      className={`rounded-2xl border-2 border-dashed p-12 text-center transition-all duration-200 hover:border-red-400 hover:-translate-y-0.5 hover:shadow-md ${
        isDragActive
          ? "border-red-500 bg-red-50"
          : "border-slate-300 bg-white"
      }`}
    >
      <input {...getInputProps()} />

      <UploadCloud
        className="mx-auto mb-5 text-red-700"
        size={42}
      />

      <h3 className="text-xl font-semibold text-slate-900">
        Drag & Drop your contract
      </h3>

      <p className="mt-2 text-slate-600">
        or
      </p>

      <button
        type="button"
        onClick={onBrowse}
        className="mt-4 rounded-xl bg-red-700 px-6 py-3 font-medium text-white transition-colors duration-200 hover:bg-red-800"
      >
        Browse Files
      </button>

      <p className="mt-6 text-sm text-slate-500">
        Supports PDF, DOCX and TXT • Maximum 10 MB
      </p>
    </section>
  );
}
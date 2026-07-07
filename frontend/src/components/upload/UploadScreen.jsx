import { useRef, useState } from "react";

import Button from "../common/Button";

import HeroSection from "./HeroSection";
import FeatureHighlights from "./FeatureHighlights";
import UploadZone from "./UploadZone";
import SelectedFile from "./SelectedFile";

export default function UploadScreen() {
  const [selectedFile, setSelectedFile] = useState(null);

  const fileInputRef = useRef(null);

  const handleBrowse = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setSelectedFile(file);
    }

    event.target.value = "";
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
  };

  return (
    <div className="space-y-12">
      <HeroSection />

      <FeatureHighlights />

      {!selectedFile ? (
        <UploadZone
          onFileSelect={setSelectedFile}
          onBrowse={handleBrowse}
        />
      ) : (
        <>
          <SelectedFile
            file={selectedFile}
            onReplace={handleBrowse}
            onRemove={handleRemoveFile}
          />

          <div className="flex justify-center">
            <Button>
              Analyze Contract
            </Button>
          </div>
        </>
      )}

      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf,.docx,.txt"
        className="hidden"
        onChange={handleFileChange}
      />
    </div>
  );
}
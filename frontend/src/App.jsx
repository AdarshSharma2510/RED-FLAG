import { useState } from "react";

import AppLayout from "./components/layout/AppLayout";
import Logo from "./components/layout/Logo";
import Footer from "./components/layout/Footer";

import UploadScreen from "./components/upload/UploadScreen";
import LoadingScreen from "./components/loading/LoadingScreen";
import ResultsScreen from "./components/results/ResultsScreen";

import { scanContract } from "./services/api";

const initialState = {
  status: "upload",
  result: null,
  error: null,
};

function App() {
  const [appState, setAppState] = useState(initialState);

  const handleAnalyze = async (file) => {
    try {
      setAppState({
        status: "loading",
        result: null,
        error: null,
      });

      const result = await scanContract(file);

      setAppState({
        status: "results",
        result,
        error: null,
      });
    } catch (error) {
      console.error(error);

      setAppState({
        status: "upload",
        result: null,
        error:
          error.response?.data?.detail ||
          "Something went wrong while analyzing the contract.",
      });
    }
  };

  const handleAnalyzeAnother = () => {
    setAppState(initialState);
  };

  return (
    <AppLayout>
      <header className="mb-16">
        <Logo />
      </header>

      <section className="flex flex-1 items-center justify-center">
        <div className="w-full max-w-6xl rounded-3xl border border-slate-200 bg-white p-10 shadow-sm">
          {appState.status === "upload" && (
            <UploadScreen
              onAnalyze={handleAnalyze}
              analyzing={false}
            />
          )}

          {appState.status === "loading" && <LoadingScreen />}

          {appState.status === "results" && (
            <ResultsScreen
              result={appState.result}
              onAnalyzeAnother={handleAnalyzeAnother}
            />
          )}
        </div>
      </section>

      <Footer />
    </AppLayout>
  );
}

export default App;
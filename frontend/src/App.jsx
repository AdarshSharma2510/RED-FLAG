import { useState } from "react";

import AppLayout from "./components/layout/AppLayout";
import Logo from "./components/layout/Logo";
import UploadScreen from "./components/upload/UploadScreen";

const initialState = {
  status: "upload",
  file: null,
  result: null,
  error: null,
};

function App() {
  const [appState, setAppState] = useState(initialState);

  return (
    <AppLayout>
      <header className="mb-16">
        <Logo />
      </header>

      <section className="flex flex-1 items-center justify-center">
        <div className="w-full max-w-5xl rounded-3xl border border-slate-200 bg-white p-10 shadow-sm">
          {appState.status === "upload" && <UploadScreen />}
        </div>
      </section>
    </AppLayout>
  );
}

export default App;
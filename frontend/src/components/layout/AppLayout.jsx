/**
 * Shared layout used across all application screens.
 */
export default function AppLayout({ children }) {
  return (
    <main className="min-h-screen bg-slate-300">
      <div className="mx-auto flex min-h-screen w-full max-w-6xl flex-col px-6 py-10 lg:px-8">
        {children}
      </div>
    </main>
  );
}
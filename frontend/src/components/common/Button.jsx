/**
 * Reusable primary button used throughout the application.
 */
export default function Button({
  children,
  onClick,
  disabled = false,
  type = "button",
  className = "",
}) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`
        inline-flex
        items-center
        justify-center
        rounded-xl
        bg-red-700
        px-6
        py-3
        text-sm
        font-semibold
        text-white
        shadow-sm
        transition-all
        duration-200
        hover:bg-red-800
        hover:shadow-md
        disabled:cursor-not-allowed
        disabled:opacity-50
        ${className}
      `}
    >
      {children}
    </button>
  );
}
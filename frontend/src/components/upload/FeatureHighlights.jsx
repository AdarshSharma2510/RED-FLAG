import {
  Brain,
  ShieldAlert,
  FileSearch,
} from "lucide-react";

const features = [
  {
    icon: Brain,
    title: "AI Analysis",
    description:
      "Leverages Google Gemini to evaluate legal contract risks.",
  },
  {
    icon: ShieldAlert,
    title: "Risk Detection",
    description:
      "Highlights high, medium and low severity legal concerns.",
  },
  {
    icon: FileSearch,
    title: "Actionable Insights",
    description:
      "Explains consequences and provides practical recommendations.",
  },
];

export default function FeatureHighlights() {
  return (
    <section className="grid gap-4 md:grid-cols-3">
      {features.map((feature) => {
        const Icon = feature.icon;

        return (
          <div
            key={feature.title}
            className="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition-all duration-200 hover:-translate-y-1 hover:shadow-md"
          >
            <Icon
              className="mb-4 text-red-700"
              size={26}
            />

            <h3 className="font-semibold text-slate-900">
              {feature.title}
            </h3>

            <p className="mt-2 text-sm leading-6 text-slate-600">
              {feature.description}
            </p>
          </div>
        );
      })}
    </section>
  );
}
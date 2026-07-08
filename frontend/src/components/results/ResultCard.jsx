import { useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";

import SeverityBadge from "./SeverityBadge";
import MetadataPill from "./MetadataPill";
import ConfidenceBadge from "./ConfidenceBadge";

export default function ResultCard({ result }) {
  const { finding, analysis } = result;

  const [expanded, setExpanded] = useState(false);

  const shouldCollapse = finding.clause_text.length > 180;

  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm transition-shadow duration-200 hover:shadow-md">

      {/* Header */}

      <div className="flex flex-wrap items-center justify-between gap-4">

        <div className="flex items-center gap-3">
          <SeverityBadge severity={finding.severity} />

          <h2 className="text-xl font-semibold text-slate-900">
            {finding.category}
          </h2>
        </div>

        <ConfidenceBadge confidence={analysis.confidence} />
      </div>

      {/* Metadata */}

      <div className="mt-6 flex flex-wrap gap-2">
{/* 
        <MetadataPill>
          Clause #{finding.clause_id}
        </MetadataPill>

        <MetadataPill>
          Sentence #{finding.sentence_id}
        </MetadataPill> */}

        {/* <MetadataPill>
          {finding.trigger_source}
        </MetadataPill> */}

      </div>

      {/* Explanation */}

      <section className="mt-8">

        <h3 className="mb-2 font-semibold text-slate-900">
          Explanation
        </h3>

        <p className="leading-7 text-slate-700">
          {finding.explanation}
        </p>

      </section>

      {/* Matched Text */}

      <section className="mt-8">

        <h3 className="mb-2 font-semibold text-slate-900">
          Matched Text
        </h3>

        <div className="rounded-xl bg-slate-50 p-4 text-slate-700">
          {finding.matched_text}
        </div>

      </section>

      {/* Clause */}

      <section className="mt-8">

        <div className="mb-2 flex items-center justify-between">

          <h3 className="font-semibold text-slate-900">
            Clause Text
          </h3>

          {shouldCollapse && (
            <button
              onClick={() => setExpanded(!expanded)}
              className="flex items-center gap-1 text-sm font-medium text-red-700 hover:text-red-800"
            >
              {expanded ? (
                <>
                  Show Less
                  <ChevronUp size={16} />
                </>
              ) : (
                <>
                  Show More
                  <ChevronDown size={16} />
                </>
              )}
            </button>
          )}

        </div>

        <div className="rounded-xl bg-slate-50 p-4 text-slate-700 leading-7">

          {shouldCollapse && !expanded
            ? `${finding.clause_text.slice(0, 180)}...`
            : finding.clause_text}

        </div>

      </section>

      {/* AI Analysis */}

      <section className="mt-10 space-y-8">

        <div>

          <h3 className="mb-2 font-semibold text-slate-900">
            Risk Summary
          </h3>

          <p className="leading-7 text-slate-700">
            {analysis.risk_summary}
          </p>

        </div>

        <div>

          <h3 className="mb-2 font-semibold text-slate-900">
            Legal Consequence
          </h3>

          <p className="leading-7 text-slate-700">
            {analysis.legal_consequence}
          </p>

        </div>

        <div>

          <h3 className="mb-2 font-semibold text-slate-900">
            Recommendation
          </h3>

          <p className="leading-7 text-slate-700">
            {analysis.recommendation}
          </p>

        </div>

      </section>

    </div>
  );
}
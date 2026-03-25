import Card from "@/components/common/Card";
import EmptyState from "@/components/common/EmptyState";

export default function EvaluationPage() {
  return (
    <div className="grid grid-2">
      <Card title="Retrieval Metrics">
        <p className="muted">Metrics cards and benchmark summaries will appear here.</p>
      </Card>

      <Card title="Answer Quality">
        <p className="muted">Answer evaluation results and feedback summaries will appear here.</p>
      </Card>

      <div style={{ gridColumn: "1 / -1" }}>
        <EmptyState
          title="Evaluation dashboard foundation ready"
          description="Next phase: connect evaluation endpoint and render benchmark cards."
        />
      </div>
    </div>
  );
}
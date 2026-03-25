import Card from "@/components/common/Card";

export default function AdminPage() {
  return (
    <Card title="Admin">
      <p className="muted">
        This page can later host index rebuild tools, ingestion triggers, system metrics, and admin-only actions.
      </p>
    </Card>
  );
}
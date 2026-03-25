import Card from "@/components/common/Card";
import EmptyState from "@/components/common/EmptyState";

export default function DocumentsPage() {
  return (
    <div className="grid" style={{ gap: 20 }}>
      <Card title="Documents">
        <p className="muted">
          This page will contain upload, filtering, listing, and document detail views for ingested financial documents.
        </p>
      </Card>

      <EmptyState
        title="Document management foundation ready"
        description="Next phase: connect UploadPanel, DocumentTable, filters, and details drawer."
      />
    </div>
  );
}
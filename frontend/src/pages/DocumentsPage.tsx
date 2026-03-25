import Card from "@/components/common/Card";
import EmptyState from "@/components/common/EmptyState";
import FileUpload from "@/components/upload/FileUpload";

export default function DocumentsPage() {
  return (
    <div className="grid" style={{ gap: 20 }}>
      <Card title="Documents">
        <p className="muted">
          Upload financial documents to start the RAG pipeline.
        </p>
      </Card>

      <FileUpload />

      <EmptyState
        title="Document management foundation ready"
        description="Next phase: connect document listing, filters, and details drawer."
      />
    </div>
  );
}
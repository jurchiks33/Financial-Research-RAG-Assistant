type UploadStatusProps = {
  loading: boolean;
  error: string | null;
  successMessage: string | null;
};

export default function UploadStatus({
  loading,
  error,
  successMessage,
}: UploadStatusProps) {
  if (loading) {
    return (
      <div
        style={{
          borderRadius: 14,
          padding: "12px 14px",
          background: "rgba(59, 130, 246, 0.08)",
          border: "1px solid rgba(59, 130, 246, 0.22)",
          color: "#bfdbfe",
          fontSize: 14,
        }}
      >
        Uploading document...
      </div>
    );
  }

  if (error) {
    return (
      <div
        style={{
          borderRadius: 14,
          padding: "12px 14px",
          background: "rgba(239, 68, 68, 0.08)",
          border: "1px solid rgba(239, 68, 68, 0.22)",
          color: "#fecaca",
          fontSize: 14,
        }}
      >
        {error}
      </div>
    );
  }

  if (successMessage) {
    return (
      <div
        style={{
          borderRadius: 14,
          padding: "12px 14px",
          background: "rgba(34, 197, 94, 0.08)",
          border: "1px solid rgba(34, 197, 94, 0.22)",
          color: "#bbf7d0",
          fontSize: 14,
        }}
      >
        {successMessage}
      </div>
    );
  }

  return null;
}
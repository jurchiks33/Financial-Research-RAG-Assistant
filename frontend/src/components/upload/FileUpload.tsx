import { useRef, useState } from "react";
import { documentService } from "../../services/documentService";
import type { DocumentUploadResponse } from "../../types/document";
import UploadStatus from "./UploadStatus";

const ACCEPTED_FILE_TYPES = ".pdf,.txt,.md,.docx";

function formatFileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
}

export default function FileUpload() {
  const inputRef = useRef<HTMLInputElement | null>(null);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [uploadedDocument, setUploadedDocument] =
    useState<DocumentUploadResponse | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0] || null;
    setSelectedFile(file);
    setError(null);
    setUploadedDocument(null);
  };

  const handleOpenFilePicker = () => {
    inputRef.current?.click();
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Please select a document first.");
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const result = await documentService.uploadDocument(selectedFile);
      setUploadedDocument(result);
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "Unexpected upload error.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        background: "#0f1b38",
        border: "1px solid rgba(120, 160, 255, 0.16)",
        borderRadius: 24,
        padding: 28,
        boxShadow: "0 10px 30px rgba(0, 0, 0, 0.18)",
      }}
    >
      <div style={{ display: "grid", gap: 10 }}>
        <h2
          style={{
            margin: 0,
            fontSize: 24,
            fontWeight: 700,
            color: "#f5f7ff",
          }}
        >
          Upload a document
        </h2>

        <p
          style={{
            margin: 0,
            color: "#98a3c7",
            fontSize: 15,
            lineHeight: 1.6,
          }}
        >
          Supported formats: PDF, TXT, MD, DOCX
        </p>
      </div>

      <input
        ref={inputRef}
        type="file"
        accept={ACCEPTED_FILE_TYPES}
        onChange={handleFileChange}
        style={{ display: "none" }}
      />

      <div style={{ marginTop: 22, display: "grid", gap: 14 }}>
        <div
          style={{
            border: "1px dashed rgba(120, 160, 255, 0.28)",
            background: "rgba(255, 255, 255, 0.02)",
            borderRadius: 18,
            padding: 18,
            display: "grid",
            gap: 14,
          }}
        >
          <div style={{ display: "flex", flexWrap: "wrap", gap: 12, alignItems: "center" }}>
            <button
              type="button"
              onClick={handleOpenFilePicker}
              style={{
                background: "#1d4ed8",
                color: "#ffffff",
                border: "none",
                borderRadius: 12,
                padding: "12px 16px",
                fontSize: 15,
                fontWeight: 600,
                cursor: "pointer",
              }}
            >
              Choose file
            </button>

            <span
              style={{
                color: selectedFile ? "#e8ecff" : "#98a3c7",
                fontSize: 15,
              }}
            >
              {selectedFile ? selectedFile.name : "No file selected"}
            </span>
          </div>

          {selectedFile && (
            <div
              style={{
                borderRadius: 16,
                background: "rgba(255,255,255,0.04)",
                border: "1px solid rgba(120, 160, 255, 0.12)",
                padding: 14,
                display: "grid",
                gap: 6,
              }}
            >
              <div style={{ color: "#f5f7ff", fontSize: 14 }}>
                <strong>File:</strong> {selectedFile.name}
              </div>
              <div style={{ color: "#b7c0dd", fontSize: 14 }}>
                <strong>Type:</strong> {selectedFile.type || "unknown"}
              </div>
              <div style={{ color: "#b7c0dd", fontSize: 14 }}>
                <strong>Size:</strong> {formatFileSize(selectedFile.size)}
              </div>
            </div>
          )}
        </div>

        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
          <button
            type="button"
            onClick={handleUpload}
            disabled={loading}
            style={{
              background: loading ? "#3a4568" : "#22c55e",
              color: "#081120",
              border: "none",
              borderRadius: 12,
              padding: "12px 18px",
              fontSize: 15,
              fontWeight: 700,
              cursor: loading ? "not-allowed" : "pointer",
              opacity: loading ? 0.7 : 1,
            }}
          >
            {loading ? "Uploading..." : "Upload document"}
          </button>
        </div>

        <UploadStatus
          loading={loading}
          error={error}
          successMessage={
            uploadedDocument
              ? `Upload successful. Document ID: ${uploadedDocument.document_id}`
              : null
          }
        />

        {uploadedDocument && (
          <div
            style={{
              borderRadius: 16,
              background: "rgba(34, 197, 94, 0.08)",
              border: "1px solid rgba(34, 197, 94, 0.25)",
              padding: 16,
              display: "grid",
              gap: 8,
            }}
          >
            <div style={{ color: "#dcfce7", fontSize: 14 }}>
              <strong>Filename:</strong> {uploadedDocument.filename}
            </div>
            <div style={{ color: "#dcfce7", fontSize: 14 }}>
              <strong>Status:</strong> {uploadedDocument.status}
            </div>
            <div style={{ color: "#bbf7d0", fontSize: 14, wordBreak: "break-word" }}>
              <strong>Stored path:</strong> {uploadedDocument.stored_path}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
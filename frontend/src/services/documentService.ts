import { api } from "@/services/api";
import type { DocumentItem, DocumentUploadResponse } from "@/types/document";

export const documentService = {
  async listDocuments(): Promise<DocumentItem[]> {
    const response = await api.get("/api/v1/documents");
    return response.data;
  },

  async uploadDocument(file: File): Promise<DocumentUploadResponse> {
    const formData = new FormData();
    formData.append("file", file);

    const response = await api.post<DocumentUploadResponse>(
      "/api/v1/documents/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return response.data;
  },
};
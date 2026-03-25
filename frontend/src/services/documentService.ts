import { api } from "@/services/api";
import type { DocumentItem } from "@/types/document";

export const documentService = {
  async listDocuments(): Promise<DocumentItem[]> {
    const response = await api.get("/api/documents");
    return response.data;
  },
};
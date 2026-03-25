import { api } from "@/services/api";
import type { RetrievalResult } from "@/types/retrieval";

export const retrievalService = {
  async search(query: string): Promise<RetrievalResult[]> {
    const response = await api.post("/api/retrieval", { query });
    return response.data;
  },
};
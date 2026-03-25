import { api } from "@/services/api";
import type { EvaluationSummary } from "@/types/evaluation";

export const evaluationService = {
  async getSummary(): Promise<EvaluationSummary> {
    const response = await api.get("/api/evaluation");
    return response.data;
  },
};
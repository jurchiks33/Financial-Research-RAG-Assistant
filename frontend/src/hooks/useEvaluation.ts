import { useQuery } from "@tanstack/react-query";
import { evaluationService } from "@/services/evaluationService";

export function useEvaluation() {
  return useQuery({
    queryKey: ["evaluation-summary"],
    queryFn: () => evaluationService.getSummary(),
  });
}
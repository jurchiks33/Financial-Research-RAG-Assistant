import { useMutation } from "@tanstack/react-query";
import { chatService } from "@/services/chatService";
import type { ChatRequest } from "@/types/chat";

export function useChat() {
  return useMutation({
    mutationFn: (payload: ChatRequest) => chatService.sendMessage(payload),
  });
}
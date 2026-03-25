import { api } from "@/services/api";
import type { ChatRequest, ChatResponse } from "@/types/chat";

export const chatService = {
  async sendMessage(payload: ChatRequest): Promise<ChatResponse> {
    const response = await api.post("/api/chat", payload);
    return response.data;
  },
};
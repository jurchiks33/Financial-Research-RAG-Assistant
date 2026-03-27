import { api } from "@/services/api";
import type {
  ChatRequest,
  ChatResponse,
  ChatQueryRequest,
  ChatQueryResponse,
} from "@/types/chat";

export const chatService = {
  async sendMessage(payload: ChatRequest): Promise<ChatResponse> {
    const response = await api.post("/api/chat", payload);
    return response.data;
  },

  async queryDocument(payload: ChatQueryRequest): Promise<ChatQueryResponse> {
    const response = await api.post<ChatQueryResponse>("/api/v1/chat/query", payload);
    return response.data;
  },
};
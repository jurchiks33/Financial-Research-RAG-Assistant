export type Citation = {
  source_id: string;
  title?: string;
  snippet?: string;
  page?: number;
};

export type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at?: string;
};

export type ChatRequest = {
  query: string;
  conversation_id?: string;
};

export type ChatResponse = {
  answer: string;
  citations: Citation[];
  conversation_id?: string;
};
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

/**
 * Phase 2 document question-answering types
 * These are added separately so existing chat code does not break.
 */
export interface ChatQueryRequest {
  question: string;
  document_id: string;
  top_k?: number;
}

export interface CitationItem {
  index: number;
  chunk_id: string;
  chunk_index: number;
  source_filename?: string;
  text: string;
  score: number;
  char_start?: number;
  char_end?: number;
}

export interface ChatQueryResponse {
  question: string;
  answer: string;
  citations: CitationItem[];
}
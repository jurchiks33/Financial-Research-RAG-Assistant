export type RetrievalResult = {
  chunk_id: string;
  document_id: string;
  score: number;
  snippet: string;
  title?: string;
};
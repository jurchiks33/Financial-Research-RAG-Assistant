export type DocumentItem = {
  id: string;
  filename: string;
  document_type?: string;
  uploaded_at?: string;
  status?: string;
};

export type DocumentUploadResponse = {
  document_id: string;
  filename: string;
  content_type: string;
  size_bytes: number;
  stored_path: string;
  status: "uploaded";
};
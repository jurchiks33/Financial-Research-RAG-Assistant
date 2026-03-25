import FileUpload from "../components/upload/FileUpload";

export default function UploadPage() {
  return (
    <main className="min-h-screen bg-slate-100 px-6 py-10">
      <div className="mx-auto max-w-5xl">
        <h1 className="mb-2 text-3xl font-bold text-slate-900">
          Phase 2 — Document Upload Flow
        </h1>
        <p className="mb-8 text-slate-600">
          Upload a document to start the RAG pipeline.
        </p>

        <FileUpload />
      </div>
    </main>
  );
}
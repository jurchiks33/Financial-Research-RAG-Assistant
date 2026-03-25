import { Routes, Route } from "react-router-dom";
import ChatPage from "@/pages/ChatPage";
import DocumentsPage from "@/pages/DocumentsPage";
import EvaluationPage from "@/pages/EvaluationPage";
import AdminPage from "@/pages/AdminPage";
import NotFoundPage from "@/pages/NotFoundPage";
import PageContainer from "@/components/layout/PageContainer";

export function AppRouter() {
  return (
    <PageContainer>
      <Routes>
        <Route path="/" element={<ChatPage />} />
        <Route path="/documents" element={<DocumentsPage />} />
        <Route path="/evaluation" element={<EvaluationPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </PageContainer>
  );
}
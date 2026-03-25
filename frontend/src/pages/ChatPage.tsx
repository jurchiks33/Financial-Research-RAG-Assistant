import Card from "@/components/common/Card";
import EmptyState from "@/components/common/EmptyState";

export default function ChatPage() {
  return (
    <div className="grid" style={{ gap: 20 }}>
      <Card title="Chat Workspace">
        <p className="muted">
          This page will host the RAG chat interface, answer cards, source citations, and conversation history.
        </p>
      </Card>

      <EmptyState
        title="Chat UI foundation ready"
        description="Next phase: build MessageList, MessageInput, AnswerCard, and connect to chat endpoint."
      />
    </div>
  );
}
import { useEffect, useState } from "react";
import { healthService } from "@/services/api";

export default function Header() {
  const [status, setStatus] = useState<"checking" | "online" | "offline">("checking");

  useEffect(() => {
    let mounted = true;

    async function checkHealth() {
      try {
        await healthService.check();
        if (mounted) setStatus("online");
      } catch {
        if (mounted) setStatus("offline");
      }
    }

    checkHealth();
    const interval = setInterval(checkHealth, 15000);

    return () => {
      mounted = false;
      clearInterval(interval);
    };
  }, []);

  return (
    <header className="header">
      <div className="container" style={{ width: "100%", margin: 0 }}>
        <div style={{ display: "flex", justifyContent: "space-between", gap: 16, alignItems: "center" }}>
          <div>
            <h1 className="title">Financial Research RAG Assistant</h1>
            <p className="subtitle">Frontend foundation for chat, document management, and evaluation workflows</p>
          </div>

          <span className="badge">
            Backend:
            <strong style={{ color: status === "online" ? "var(--success)" : status === "offline" ? "var(--danger)" : "var(--warning)" }}>
              {status}
            </strong>
          </span>
        </div>
      </div>
    </header>
  );
}
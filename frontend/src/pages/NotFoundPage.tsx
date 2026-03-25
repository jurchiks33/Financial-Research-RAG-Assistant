import { Link } from "react-router-dom";
import Card from "@/components/common/Card";

export default function NotFoundPage() {
  return (
    <Card title="Page not found">
      <p className="muted">The page you requested does not exist.</p>
      <Link to="/" className="btn" style={{ display: "inline-block", marginTop: 12 }}>
        Go back home
      </Link>
    </Card>
  );
}
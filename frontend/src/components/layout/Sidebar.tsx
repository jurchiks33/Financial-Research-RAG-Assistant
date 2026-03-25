import { NavLink } from "react-router-dom";

const navItems = [
  { to: "/", label: "Chat" },
  { to: "/documents", label: "Documents" },
  { to: "/evaluation", label: "Evaluation" },
  { to: "/admin", label: "Admin" },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div>
        <h2 style={{ margin: 0 }}>Financial RAG</h2>
        <p className="muted" style={{ marginTop: 8 }}>
          Research assistant frontend
        </p>
      </div>

      <nav className="nav-links">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === "/"}
            className={({ isActive }) =>
              `nav-link${isActive ? " active" : ""}`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
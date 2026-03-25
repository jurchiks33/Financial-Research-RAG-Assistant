import Sidebar from "@/components/layout/Sidebar";
import Header from "@/components/layout/Header";

type Props = {
  children: React.ReactNode;
};

export default function PageContainer({ children }: Props) {
  return (
    <div className="page-shell">
      <Sidebar />
      <div className="main-area">
        <Header />
        <main className="page-content">{children}</main>
      </div>
    </div>
  );
}
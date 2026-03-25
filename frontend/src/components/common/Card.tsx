type Props = {
  title?: string;
  children: React.ReactNode;
};

export default function Card({ title, children }: Props) {
  return (
    <section className="card">
      {title ? <h3 className="section-title">{title}</h3> : null}
      {children}
    </section>
  );
}
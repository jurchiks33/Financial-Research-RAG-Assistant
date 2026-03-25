type Props = {
  title: string;
  description?: string;
};

export default function EmptyState({ title, description }: Props) {
  return (
    <div className="card">
      <h3 className="section-title">{title}</h3>
      {description ? <p className="muted">{description}</p> : null}
    </div>
  );
}
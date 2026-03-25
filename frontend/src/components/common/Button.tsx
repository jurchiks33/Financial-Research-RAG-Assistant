type Props = React.ButtonHTMLAttributes<HTMLButtonElement>;

export default function Button({ children, className = "", ...props }: Props) {
  return (
    <button className={`btn ${className}`.trim()} {...props}>
      {children}
    </button>
  );
}
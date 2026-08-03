import styles from "./page.module.css";

const appName = process.env.NEXT_PUBLIC_APP_NAME;

if (!appName) {
  throw new Error(
    "Variável de ambiente obrigatória NEXT_PUBLIC_APP_NAME não definida. Veja .env.example."
  );
}

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <p className={styles.appName}>{appName}</p>
        <h1 className={styles.title}>Hello from Claude Code</h1>
      </main>
    </div>
  );
}

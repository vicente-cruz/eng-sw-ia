import styles from "./Navbar.module.css";

export default function Navbar() {
  return (
    <header className={styles.navbar}>
      <div className={styles.inner}>
        <span className={styles.brand}>
          <span className={styles.brandDot} />
          NEXUS
        </span>
        <button type="button" className={styles.loginButton}>
          Login
        </button>
      </div>
    </header>
  );
}

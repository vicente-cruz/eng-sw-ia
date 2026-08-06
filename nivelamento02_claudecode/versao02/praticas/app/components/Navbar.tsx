"use client";

import { useEffect, useRef, useState } from "react";

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsMenuOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <header className="animate-navbar-gradient sticky top-0 z-50 flex h-16 w-full shrink-0 items-center justify-between border-b border-white/10 bg-gradient-to-r from-cyan-600/50 via-fuchsia-600/40 to-purple-700/50 px-6 backdrop-blur-md">
      <span className="text-lg font-semibold tracking-wide text-white">
        Claude<span className="text-cyan-400">Code</span>
      </span>

      <div ref={menuRef} className="relative">
        <button
          onClick={() => setIsMenuOpen((open) => !open)}
          className="flex items-center gap-2 rounded-full border border-cyan-400/50 bg-cyan-400/10 px-5 py-2 text-sm font-medium text-cyan-300 shadow-[0_0_15px_rgba(34,211,238,0.35)] transition-colors hover:bg-cyan-400/20 hover:shadow-[0_0_25px_rgba(34,211,238,0.55)]"
        >
          Login
        </button>

        {isMenuOpen && (
          <div className="absolute right-0 mt-2 w-44 overflow-hidden rounded-xl border border-white/10 bg-slate-950/90 py-1 shadow-[0_0_25px_rgba(34,211,238,0.15)] backdrop-blur-md">
            <button className="block w-full px-4 py-2 text-left text-sm text-slate-200 transition-colors hover:bg-cyan-400/10 hover:text-cyan-300">
              Perfil
            </button>
            <div className="my-1 h-px bg-white/10" />
            <button className="block w-full px-4 py-2 text-left text-sm text-red-400 transition-colors hover:bg-red-500/10 hover:text-red-300">
              Logout
            </button>
          </div>
        )}
      </div>
    </header>
  );
}

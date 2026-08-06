"use client";

import { useRef, useState, type MouseEvent } from "react";

export default function Home() {
  const containerRef = useRef<HTMLDivElement>(null);
  const [offset, setOffset] = useState({ x: 0, y: 0 });

  function handleMouseMove(event: MouseEvent<HTMLDivElement>) {
    const bounds = containerRef.current?.getBoundingClientRect();
    if (!bounds) return;
    setOffset({
      x: (event.clientX - bounds.left) / bounds.width - 0.5,
      y: (event.clientY - bounds.top) / bounds.height - 0.5,
    });
  }

  function handleMouseLeave() {
    setOffset({ x: 0, y: 0 });
  }

  return (
    <div
      ref={containerRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      className="relative flex flex-1 items-center justify-center overflow-hidden bg-slate-950"
    >
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,255,255,0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,255,255,0.06)_1px,transparent_1px)] bg-[size:48px_48px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_50%,black_40%,transparent_100%)]" />

      <div
        style={{ transform: `translate(${offset.x * 120}px, ${offset.y * 120}px)` }}
        className="absolute -top-32 -left-32 h-96 w-96 transition-transform duration-300 ease-out"
      >
        <div className="animate-pulse-glow h-full w-full rounded-full bg-cyan-500/30 blur-3xl" />
      </div>

      <div
        style={{ transform: `translate(${offset.x * -100}px, ${offset.y * -100}px)` }}
        className="absolute -right-32 -bottom-32 h-96 w-96 transition-transform duration-300 ease-out"
      >
        <div className="animate-pulse-glow h-full w-full rounded-full bg-fuchsia-500/30 blur-3xl [animation-delay:2s]" />
      </div>

      <h1 className="relative z-10 bg-gradient-to-r from-cyan-300 via-white to-fuchsia-300 bg-clip-text px-6 text-center text-5xl font-extrabold tracking-tight text-transparent drop-shadow-[0_0_25px_rgba(34,211,238,0.35)] sm:text-7xl">
        Hello from Claude Code
      </h1>
    </div>
  );
}

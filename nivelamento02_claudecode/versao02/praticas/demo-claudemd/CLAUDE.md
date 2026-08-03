# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- `npm run dev` — starts the dev server on **port 4000** (not the Next.js default 3000; configured via `next dev -p 4000` in `package.json`).
- `npm run build` — production build. This will **fail** if `NEXT_PUBLIC_APP_NAME` is not set (see Environment variables below).
- `npm run start` — serves the production build.
- `npm run lint` — runs ESLint (`eslint-config-next`, flat config in `eslint.config.mjs`).

There is no test suite configured in this project.

## Environment variables

- `NEXT_PUBLIC_APP_NAME` is **required**. `src/app/page.tsx` reads it at module load and throws if it is unset, which fails both `next dev` and `next build`.
- Copy `.env.example` to `.env.local` before running any script:
  ```bash
  cp .env.example .env.local
  ```

## Architecture

Minimal Next.js App Router project (TypeScript, no Tailwind):

- `src/app/page.tsx` — home page (server component). Reads `NEXT_PUBLIC_APP_NAME` directly from `process.env` and fails fast if missing.
- `src/app/layout.tsx` — root layout, loads Geist fonts via `next/font/google`.
- `src/app/page.module.css` — CSS Modules styling for the home page (animated gradient background).
- Path alias `@/*` maps to `src/*` (`tsconfig.json`).

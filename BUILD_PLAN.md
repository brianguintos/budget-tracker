# Build plan — Budget Tracker v1

Total: ~10–15 hours across 4 sessions. Each session ends with working,
committed code. Ask Muse to review the code and help debug — but write it
yourself: you'll need to explain every design decision in interviews.

## Session 1 — Database + backend skeleton (~3h)

- [ ] Install PostgreSQL locally; `createdb budget_tracker`
- [ ] Write `backend/schema.sql`: tables `categories(id, name, color)` and
      `transactions(id, amount, date, note, category_id → categories)`
- [ ] `psql budget_tracker < backend/schema.sql`; verify with `\dt`
- [ ] FastAPI skeleton: `app/main.py` health endpoint, `app/database.py`
      engine + session wired to `DATABASE_URL` from `.env`
- [ ] `GET /health` returns `{"status": "ok"}`; commit: `feat: backend skeleton + schema`

## Session 2 — Transactions API (~3–4h)

- [ ] SQLAlchemy models in `app/models.py`; Pydantic schemas in `app/schemas.py`
- [ ] Endpoints: `POST /transactions`, `GET /transactions` (filter by month),
      `GET /transactions/{id}`, `PUT /transactions/{id}`, `DELETE /transactions/{id}`
- [ ] Test every endpoint in the auto docs at `/docs`; commit per endpoint group

## Session 3 — Categories API + seed data (~2–3h)

- [ ] Categories CRUD: `POST/GET/PUT/DELETE /categories`
- [ ] `backend/seed.sql`: ~8 categories, ~40 realistic transactions across 3 months
- [ ] Monthly totals endpoint: `GET /summary?year=2026&month=10` →
      totals per category + grand total
- [ ] Commit: `feat: categories, seed data, monthly summary endpoint`

## Session 4 — React front end (~4–5h)

- [ ] `npm create vite@latest` choices already reflected in `frontend/package.json`
- [ ] `TransactionList` (with month filter), `TransactionForm` (add/edit),
      `CategoryList`, `MonthlySummary` (per-category totals + simple bar chart —
      plain divs with widths, no chart lib needed for v1)
- [ ] `src/api/client.js` wraps `fetch` against `http://localhost:8000`
- [ ] End-to-end: add a transaction in the UI, see it in the summary; commit

## v1 done when

- [ ] README run instructions work on a fresh machine
- [ ] Seed data loads; UI shows monthly summary correctly
- [ ] Commit history shows your own step-by-step work
- [ ] Repo is public on GitHub and pinned on your profile

## Interview lines this project earns you

- "I designed the schema — transactions reference categories with a foreign key,
  and I kept amounts as NUMERIC to avoid float rounding."
- "The summary endpoint aggregates in SQL with GROUP BY rather than in Python,
  so the database does the heavy lifting."
- "The front end fetches fresh data per view — no stale state bugs."

# Budget Tracker — built for real

A personal budget tracker with a **React** front end, a **Python (FastAPI)** REST API,
and **PostgreSQL**. Built from scratch by Brian Guintos (Oct 2026) — own code, own
commits. This repo is the scaffold: structure, schema, and a session-by-session
build plan. Every feature is a TODO for you to implement.

## Stack (matches the application claim: React + Python + PostgreSQL)

- **Frontend:** React (Vite) — `frontend/`
- **Backend:** FastAPI — `backend/`
- **Database:** PostgreSQL — schema in `backend/schema.sql`

## Quick start (once implemented)

```bash
# 1. Database
createdb budget_tracker
psql budget_tracker < backend/schema.sql
psql budget_tracker < backend/seed.sql   # optional demo data

# 2. Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # set DATABASE_URL
uvicorn app.main:app --reload
# API docs: http://localhost:8000/docs

# 3. Frontend
cd frontend
npm install
npm run dev
```

## v1 scope (10–15 hours, 4 sessions — see BUILD_PLAN.md)

1. Transactions CRUD (add / edit / delete, amount, date, note)
2. Categories CRUD + assign each transaction a category
3. Monthly summary view (totals per category, simple bar chart)
4. README run instructions + seed data + clean commit history

## Stretch (only after v1 works)

- User accounts (login), multiple wallets/accounts, CSV import/export,
  recurring transactions, budget limits per category with warnings.

## Make this repo yours

```bash
cd budget-tracker-build
git init
git add .
git commit -m "chore: initial scaffold"
# create an empty repo named budget-tracker on github.com/brianguintos, then:
git remote add origin git@github.com:brianguintos/budget-tracker.git
git branch -M main
git push -u origin main
```

Commit as you go — one commit per finished piece. You'll talk about this project
in interviews, so the commits and the code need to be yours.

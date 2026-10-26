"""FastAPI app. TODO(Session 2-3): add transaction + category routers."""
from fastapi import FastAPI

app = FastAPI(title="Budget Tracker API")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO(Session 2): transactions router
#   POST   /transactions
#   GET    /transactions?year=2026&month=10
#   GET    /transactions/{id}
#   PUT    /transactions/{id}
#   DELETE /transactions/{id}

# TODO(Session 3): categories router + summary endpoint
#   GET    /summary?year=2026&month=10  -> per-category totals + grand total

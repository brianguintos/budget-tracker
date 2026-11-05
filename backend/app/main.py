"""FastAPI app. TODO(Session 2-3): add transaction + category routers."""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db

app = FastAPI(title="Budget Tracker API")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/transactions", response_model=schemas.TransactionOut, status_code=201) #function to create a transaction, declares response model and status code 
def create_transaction(payload: schemas.TransactionCreate, db: Session = Depends(get_db)): #
    transaction = models.Transaction(**payload.model_dump())
    db.add(transaction) 
    db.commit()
    db.refresh(transaction)
    return transaction

# TODO(Session 2): transactions router
#   POST   /transactions
#   GET    /transactions?year=2026&month=10
#   GET    /transactions/{id}
#   PUT    /transactions/{id}
#   DELETE /transactions/{id}

# TODO(Session 3): categories router + summary endpoint
#   GET    /summary?year=2026&month=10  -> per-category totals + grand total

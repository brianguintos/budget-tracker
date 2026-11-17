"""FastAPI app. TODO(Session 2-3): add transaction + category routers."""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import extract
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

@app.get("/transactions/{transaction_id}", response_model=schemas.TransactionOut) #function to get a transaction by id, declares response model
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.get("/transactions", response_model=list[schemas.TransactionOut])
def list_transactions(year: int | None = None, month: int | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Transaction)
    if year is not None:
        query = query.filter(extract("year", models.Transaction.date) == year)
    if month is not None:
        query = query.filter(extract("month", models.Transaction.date) == month)
    return query.order_by(models.Transaction.date).all()

# TODO(Session 2): transactions router
#   POST   /transactions
#   GET    /transactions?year=2026&month=10
#   GET    /transactions/{id}
#   PUT    /transactions/{id}
#   DELETE /transactions/{id}

# TODO(Session 3): categories router + summary endpoint
#   GET    /summary?year=2026&month=10  -> per-category totals + grand total

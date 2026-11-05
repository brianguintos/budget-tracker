"""Pydantic request/response schemas. TODO(Session 2): implement."""
from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class TransactionCreate(BaseModel):
        amount: Decimal
        date: date
        note: str = ""
        category_id: int
    # TODO: amount, date, note, category_id


class TransactionOut(TransactionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    # TODO: id, created_at
    pass

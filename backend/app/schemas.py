"""Pydantic request/response schemas. TODO(Session 2): implement."""
from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    # TODO: amount, date, note, category_id
    pass


class TransactionOut(TransactionCreate):
    # TODO: id, created_at
    pass

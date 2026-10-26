"""SQLAlchemy models. TODO(Session 2): implement Category and Transaction."""
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import relationship

from .database import Base


class Category(Base):
    __tablename__ = "categories"
    # TODO: id, name, color, created_at + relationship to transactions


class Transaction(Base):
    __tablename__ = "transactions"
    # TODO: id, amount (Numeric!), date, note, category_id FK + relationship

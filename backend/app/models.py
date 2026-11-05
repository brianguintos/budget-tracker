"""SQLAlchemy models. TODO(Session 2): implement Category and Transaction."""
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, Text, func
from sqlalchemy.orm import relationship

from .database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False, unique=True)
    color = Column(Text, nullable=False, default="#888888")
    created_at = Column(DateTime (timezone=True), nullable=False, server_default=func.now())
    transactions = relationship("Transaction", back_populates="category")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(12, 2), nullable=False)
    date = Column(Date, nullable=False)
    note = Column(Text, nullable=False, default="")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="transactions")
    # TODO: id, amount (Numeric!), date, note, category_id FK + relationship

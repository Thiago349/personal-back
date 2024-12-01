from alchemy import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, String, Integer


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    branch = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), server_default=None)
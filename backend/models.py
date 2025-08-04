from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # "admin" or "shareholder"
    shareholder = relationship("Shareholder", uselist=False, back_populates="user")

class Shareholder(Base):
    __tablename__ = "shareholders"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="shareholder")
    issuances = relationship("Issuance", back_populates="shareholder")

class Issuance(Base):
    __tablename__ = "issuances"
    id = Column(Integer, primary_key=True, index=True)
    shareholder_id = Column(Integer, ForeignKey("shareholders.id"))
    shares = Column(Integer)
    price = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    shareholder = relationship("Shareholder", back_populates="issuances")


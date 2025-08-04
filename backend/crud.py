from sqlalchemy.orm import Session
from models import Shareholder, Issuance, User
from schemas import ShareholderCreate, IssuanceCreate
from utils import create_pdf_certificate
from fastapi import HTTPException

def get_shareholders(db: Session):
    return db.query(Shareholder).all()

def create_shareholder(db: Session, sh: ShareholderCreate):
    user = User(username=sh.email, hashed_password="$2b$12$fakehash", role="shareholder")
    db.add(user)
    db.flush()  # Récupère l'ID de l'utilisateur
    shareholder = Shareholder(name=sh.name, email=sh.email, user_id=user.id)
    db.add(shareholder)
    db.commit()
    db.refresh(shareholder)
    return shareholder

def get_issuances(db: Session, user: User):
    if user.role == "admin":
        return db.query(Issuance).all()
    elif user.role == "shareholder":
        shareholder = db.query(Shareholder).filter_by(user_id=user.id).first()
        return db.query(Issuance).filter_by(shareholder_id=shareholder.id).all()
    else:
        raise HTTPException(status_code=403, detail="Access denied")

def create_issuance(db: Session, data: IssuanceCreate):
    shareholder = db.query(Shareholder).filter_by(id=data.shareholder_id).first()
    if not shareholder:
        raise HTTPException(status_code=404, detail="Shareholder not found")
    if data.shares <= 0:
        raise HTTPException(status_code=400, detail="Invalid number of shares")
    issuance = Issuance(**data.dict())
    db.add(issuance)
    db.commit()
    db.refresh(issuance)
    return issuance

def generate_certificate(db: Session, issuance_id: int):
    issuance = db.query(Issuance).filter_by(id=issuance_id).first()
    if not issuance:
        return None
    return create_pdf_certificate(issuance)

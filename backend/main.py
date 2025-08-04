import os
import numpy as np
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
import models, schemas, crud, auth
from database import engine, get_db
from database import SessionLocal
from auth import get_password_hash
from models import User

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/token/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.authenticate_user(db, form_data.username, form_data.password)

@app.get("/api/shareholders/")
def list_shareholders(db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    return crud.get_shareholders(db)

@app.post("/api/shareholders/")
def create_shareholder(sh: schemas.ShareholderCreate, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    return crud.create_shareholder(db, sh)

@app.get("/api/issuances/")
def list_issuances(db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    return crud.get_issuances(db, user)

@app.post("/api/issuances/")
def issue_shares(issue: schemas.IssuanceCreate, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    return crud.create_issuance(db, issue)

@app.get("/api/issuances/{issuance_id}/certificate/")
def get_certificate(issuance_id: int, db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    return FileResponse(crud.generate_certificate(db, issuance_id))


def init_admin():
    db = SessionLocal()
    admin_user = db.query(User).filter(User.username == "admin").first()
    if not admin_user:
        new_admin = User(
            username="admin",
            hashed_password=get_password_hash("secret"),
            role="admin"
        )
        db.add(new_admin)
        db.commit()
        print("✅ Utilisateur admin créé avec succès !")
    else:
        print("ℹ️ Utilisateur admin déjà existant.")
    db.close()

# Appelé au démarrage
init_admin()

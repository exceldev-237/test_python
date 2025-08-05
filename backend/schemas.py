from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    username: str

class ShareholderBase(BaseModel):
    name: str
    email: str

class ShareholderCreate(ShareholderBase):
    pass

class Shareholder(ShareholderBase):
    id: int
    class Config:
        from_attributes = True

class IssuanceBase(BaseModel):
    num_shares: int
    price_per_share: float

class IssuanceCreate(IssuanceBase):
    shareholder_id: int

class Issuance(IssuanceBase):
    id: int
    date: datetime
    class Config:
        from_attributes = True

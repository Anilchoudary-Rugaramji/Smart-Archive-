from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


# --- User schemas ---


class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    """
    email: EmailStr
    password: str


class UserOut(BaseModel):
    """
    Schema for returning user information (safe for public use).
    """
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


# --- Document schemas ---

class DocumentBase(BaseModel):
    """
    Base schema for document information. Shared across input/output.
    """
    filename: str
    content: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[str] = None


class DocumentCreate(DocumentBase):
    """
    Schema for creating a new document.
    """
    pass


class DocumentOut(DocumentBase):
    """
    Schema for returning document details (including metadata).
    """
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

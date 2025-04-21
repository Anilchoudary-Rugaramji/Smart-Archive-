from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.schemas import DocumentCreate


def create_document(db: Session, document: DocumentCreate, user_id: int):
    db_document = Document(
        filename=document.filename,
        content=document.content,
        summary=document.summary,
        tags=document.tags,
        owner_id=user_id
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document_by_id(db: Session, document_id: int):
    return db.query(Document).filter(Document.id == document_id).first()


def get_documents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Document).offset(skip).limit(limit).all()


def update_document(db: Session, document_id: int, document: DocumentCreate):
    db_document = db.query(Document).filter(Document.id == document_id).first()
    if db_document:
        db_document.filename = document.filename,
        db_document.content = document.content,
        db_document.summary = document.summary,
        db_document.tags = document.tags,
        db.commit()
        db.refresh(db_document)
        return db_document
    return None


def delete_document(db: Session, document_id: int):
    db_document = db.query(document_id).filter(
        Document.id == document_id).first()
    if db_document:
        db.delete(db_document)
        db.commit()
        return db_document
    return None

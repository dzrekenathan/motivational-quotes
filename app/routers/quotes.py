from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from app import models, schemas, database


router = APIRouter(
    prefix="/quotes",
    tags=["Quotes"]
)




@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.QuoteResponse])
def get_quote(db: Session = Depends(get_db)):
    quotes = db.query(models.Quote).all()
    if not quotes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No quotes found")
    return quotes


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.QuoteResponse)
def get_single_quote(id: int, db: Session = Depends(get_db)):
    quote = db.query(models.Quote).filter(models.Quote.id == id).first()
    if not quote:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    return quote


@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.QuoteResponse)
def update_quote(id: int, quote: schemas.QuoteBase, db: Session = Depends(get_db)):
    quote_query = db.query(models.Quote).filter(models.Quote.id == id)
    if not quote:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    quote_query.update(quote.dict(), synchronize_session=False)
    db.commit()
    return quote_query.first()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_quote(id: int, db: Session = Depends(get_db)):
    quote = db.query(models.Quote).filter(models.Quote.id == id)
    if not quote.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    quote.delete(synchronize_session=False)
    db.commit()
    return

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.QuoteResponse)
def create_quote(quote: schemas.QuoteBase, db: Session = Depends(get_db)):
    new_quote = models.Quote(**quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote
















# @router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.QuoteBase])
# def get_quote(db: Session = Depends(get_db)):
#     quote = db.query(models.Quote).all()
#     if not quote:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No quotes found")
#     return quote

# @router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.QuoteResponse)
# def get_quote(id: int, db: Session = Depends(get_db)):
#     quote = db.query(models.Quote).filter(models.Quote.id == id).first()
#     if not quote:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
#     return quote

# @router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.QuoteResponse)
# def create_quote(quote: schemas.QuoteBase, db: Session = Depends(get_db)):
#     new_quote = models.Quote(**quote.dict())
#     db.add(new_quote)
#     db.commit()
#     db.refresh(new_quote)
#     return new_quote

# @router.put('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.QuoteResponse)
# def update_quote(id: int, quote: schemas.QuoteBase, db: Session = Depends(get_db)):
#     quote_query = db.query(models.Quote).filter(models.Quote.id == id)
#     if not quote:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    
#     quote_query.update(quote.dict(), synchronize_session=False)
#     db.commit()
#     return quote_query.first()
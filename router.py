from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestProduct, Response
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get(db: Session = Depends(get_db)):
    _product = crud.get_product(db, 0, 100)
    return Response(code=200, status="ok", message="Products fetched successfully", result=_product) \
        .dict(exclude_none=True)


@router.post("/create")
async def create(request: RequestProduct, db: Session = Depends(get_db)):
    crud.create_product(db=db, product=request.parameter)
    return Response(code=200, status="ok", message="Products fetched successfully") \
        .dict(exclude_none=True)


@router.delete("/delete")
async def delete(product_id: int, request: RequestProduct, db: Session = Depends(get_db)):
    crud.remove_product(product_id=product_id, db=db)
    return Response(code=200, status="ok", message="Product deleted successfully") \
        .dict(exclude_none=True)

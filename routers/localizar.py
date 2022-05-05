from fastapi import APIRouter
from data import fake_db


router = APIRouter()
a = fake_db.consulta_db()


@router.get("/v1/localiza/")
def localiza():
    return a


'''Imports'''
from fastapi import FastAPI
from routers import localizar
from services.auth import auth0

auth0()
app = FastAPI()

app.include_router(localizar.router)

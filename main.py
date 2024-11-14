from fastapi import FastAPI
from src.routers.user import Urvish

app = FastAPI()

app.include_router(Urvish)


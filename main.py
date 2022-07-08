import os.path
import random
import sys
import json
from turtle import mode
from urllib.parse import urlparse
from typing import Optional

from datetime import datetime
from pydantic import BaseModel
import uvicorn

from fastapi import FastAPI, Cookie, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException

from sqlalchemy.orm import Session

from v1.endpoints.astroapi.r_astroapi import router_astroapi


# Нужно, чтобы все модули нормально импортировались
src_dir = os.path.normpath(os.path.join(__file__, os.path.pardir))
sys.path.append(src_dir)


app = FastAPI()
app.mount("/_static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(router_astroapi) # Тарифы



class Prediction(BaseModel):
    ''' Класс с предсказанииями '''

    random_string: str = None
    health: str = None
    emotions: str = None
    personal_life: str = None
    profession: str = None
    travel: str = None
    luck: str = None


class PredictionFull(BaseModel):
    status: bool = False
    sun_sign: str = None
    prediction_date: datetime
    prediction: Prediction


@app.get('/', tags=['Root'])
async def root(request: Request):
    return {"error": False, "msg": "Fake API for testing v.0.0.1", "random": random.random()}


@app.post('/test', tags=['Test'], response_model=PredictionFull)
async def test(py_model: PredictionFull):
    return py_model

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=4040)
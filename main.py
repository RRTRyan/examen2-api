from fastapi import FastAPI
from starlette.responses import Response, JSONResponse
from starlette.requests import Request
from typing import List
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping() -> Response:
    return Response(status_code=200, content=f"pong", media_type="text/plain")

@app.get("/health")
def health() -> Response:
    return Response(status_code=200, content="Ok", media_type="text/plain")

class CharachteristicsModel(BaseModel):
    ram_memory: int
    rom_memory: int

class PhoneModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: CharachteristicsModel

phone_list: List[PhoneModel] = []

def phone_model_serialization():
    serialized_phone_model = []
    for phone_model in phone_list:
        serialized_phone_model.append(phone_model.model_dump_json())
    return serialized_phone_model

@app.post("/phones")
def post_phones(payload: List[PhoneModel]) -> JSONResponse:
    phone_list.extend(payload)
    return JSONResponse(status_code=201, content={"phones": phone_model_serialization()}, media_type="application/json")

@app.get("/phones")
def get_phones():
    return JSONResponse(status_code=200, content={"phones": phone_model_serialization()}, media_type="application/json")
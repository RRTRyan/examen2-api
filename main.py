from fastapi import FastAPI
from starlette.responses import Response, JSONResponse
from starlette.requests import Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping() -> Response:
    return Response(status_code=200, content=f"pong", media_type="text/plain")

import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


class MyMiddleaware(BaseHTTPMiddleware):
    async def dispatch(self, request:Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    
origins=["http://localhost:8000","http://localhost:5173"]
app.add_middleware(MyMiddleaware)
app.add_middleware(CORSMiddleware, allow_origins=origins)


@app.get("/blah")
async def blah():
    return {"hello":"world"}

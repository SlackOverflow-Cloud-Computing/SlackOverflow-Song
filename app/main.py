import logging
from fastapi import Depends, FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.routers import song

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(song.router)

logging.basicConfig(level=logging.INFO, format="\n%(asctime)s - %(message)s\n")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {request.method} {request.url}")
    return response


@app.get("/")
async def root():
    return {"message": "Song service is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)




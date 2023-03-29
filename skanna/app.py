from fastapi import FastAPI
from appl.server.routers.product import router as JumiaRouter

app = FastAPI()

app.include_router(JumiaRouter, tags=["Jumia"], prefix="/jumia")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}
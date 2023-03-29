import uvicorn
from fastapi import FastAPI
from skanna.routers.product import router as JumiaRouter

app = FastAPI()

app.include_router(JumiaRouter, tags=["Jumia"], prefix="/jumia")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("server.app:app", port=8000, log_level="info", reload=True)
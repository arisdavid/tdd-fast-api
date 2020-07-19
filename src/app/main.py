import uvicorn
from fastapi import FastAPI
from src.app.api import notes, ping
from src.app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])

if __name__ == "__main__":
    uvicorn.run(app=app)

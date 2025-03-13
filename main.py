from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

from router import router as tasks_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищенна ++COMPLETED++")
    await create_tables()
    print("База готова!!++START++")
    yield
    print("Выключение__EXIT__")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

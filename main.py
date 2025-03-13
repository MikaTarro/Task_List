from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

tasks = []

@app.post("/tasks")
async def add_task(task: STaskAdd):
    tasks.append(task)
    return {"ok": True, "task": task}

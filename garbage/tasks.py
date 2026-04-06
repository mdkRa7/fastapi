import asyncio
from asyncio import create_task
from fastapi import BackgroundTasks


from fastapi import FastAPI
from time import sleep


app = FastAPI()

def sync_task():
    sleep(3)
    print("something")

async def async_task():
    await asyncio.sleep(3)
    print("something")

@app.post("/")
async def some_kode(bg: BackgroundTasks):
    ...
    # asyncio.create_task(async_task())
    bg.add_task(sync_task)
    return {"success":"True"}
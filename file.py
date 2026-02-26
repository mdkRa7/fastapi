from fastapi import FastAPI, UploadFile
from starlette.responses import FileResponse, StreamingResponse

app = FastAPI()

@app.post("/file")
async def uploated_file(up: UploadFile):
    filename = up.filename
    up_file = up.file
    with open(f"new_{filename}", "wb") as f:
        f.write(up_file.read())

    return {"success:" "True"}

@app.post("/multiple_files")
async def upload_files(up: list[UploadFile]):
    for ind, filik in enumerate(up):
        with open(f"{ind}_{filik.filename}", "wb") as f:
            f.write(filik.file.read())

@app.get("/files/{filename}")
async def get_file(filename: str):
    return FileResponse(filename)


def iter_file(file):
    with open(file, "rb") as file:
        while chunk := file.read(1024*1024):
            yield chunk

@app.get("/files/streaming/{filename}")
async def get_chunks(filename: str):
    return StreamingResponse(iter_file(filename), media_type="video/mp4")

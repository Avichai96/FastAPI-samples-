from fastapi import FastAPI
from fastapi.responses import FileResponse

import os

app = FastAPI()

path = r"./"

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/file")
def get_file():
    file_path = os.path.join(path, "cat.jpg")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg")
    return {"error": "no such image"}
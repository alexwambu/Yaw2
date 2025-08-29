from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from video_pipeline import generate_video

app = FastAPI()

# Serve React build
app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

@app.get("/")
async def serve_root():
    return FileResponse("dist/index.html")

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    script = data.get("script", "")
    output = generate_video(script)
    return {"status": "done", "file": output}

from fastapi import FastAPI, UploadFile, File
from moviepy.editor import VideoFileClip, concatenate_videoclips
import uvicorn
import os

app = FastAPI()

# simple root check
@app.get("/")
def read_root():
    return {"status": "Video Creator API is running!"}

# endpoint to upload and trim video
@app.post("/process")
async def process_video(file: UploadFile = File(...)):
    input_path = f"temp_{file.filename}"
    output_path = "output.mp4"

    # save uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # load video using moviepy
    clip = VideoFileClip(input_path)

    # Example: trim first 10 seconds
    final_clip = clip.subclip(0, min(10, clip.duration))

    # write output
    final_clip.write_videofile(output_path, codec="libx264")

    # cleanup
    clip.close()
    os.remove(input_path)

    return {"output_file": output_path, "duration": final_clip.duration}

if __name__ == "__main__":
    # when running locally
    uvicorn.run(app, host="0.0.0.0", port=10000)

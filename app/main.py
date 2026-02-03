from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app.mount("/public", StaticFiles(directory=BASE_DIR / "public"), name="public")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


from app.ideas import generate_ai_idea

app = FastAPI(title="Vibe Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.get("/idea")
def get_idea(vibe: str = "normal"):
    return {"idea": generate_ai_idea(vibe)}

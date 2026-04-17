from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import anthropic
import os

app = FastAPI(title="QA Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── REQUEST MODEL ──
class ChatRequest(BaseModel):
    system: str
    message: str
    max_tokens: int = 1000

# ── CHAT ENDPOINT ──
@app.post("/api/chat")
async def chat(req: ChatRequest):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=req.max_tokens,
        system=req.system,
        messages=[{"role": "user", "content": req.message}]
    )
    return {"content": response.content[0].text}

# ── HEALTH CHECK ──
@app.get("/health")
def health():
    return {"status": "ok", "service": "QA Intelligence"}

# ── SERVE FRONTEND (must be last) ──
app.mount("/", StaticFiles(directory="static", html=True), name="static")

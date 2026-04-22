from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import anthropic
import os
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    system: str
    message: str
    max_tokens: int = 1000

@app.post("/api/chat")
async def chat(req: ChatRequest):
    try:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return JSONResponse(status_code=500, content={"error": "ANTHROPIC_API_KEY not set"})
        
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=req.max_tokens,
            system=req.system,
            messages=[{"role": "user", "content": req.message}]
        )
        return {"content": response.content[0].text}
    except Exception as e:
        print(f"ERROR: {traceback.format_exc()}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/health")
def health():
    return {"status": "ok"}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai_helper import get_llm_response
from model import predict_response_type

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CounselorInput(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_advice(data: CounselorInput):
    advice = get_llm_response(data.prompt)
    return {"advice": advice}

@app.post("/predict-response-type")
async def classify_response(data: CounselorInput):
    label = predict_response_type(data.prompt)
    return {"response_type": label}

import joblib
from pathlib import Path

# Load once at startup
MODEL_PATH = Path(__file__).parent / "response_type_model.pkl"
model = joblib.load(MODEL_PATH)

def predict_response_type(text: str) -> str:
    pred = model.predict([text])[0]
    return "direct" if pred == 1 else "indirect"

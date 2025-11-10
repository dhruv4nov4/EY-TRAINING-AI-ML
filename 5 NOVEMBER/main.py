from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.models.train import train_model
from app.explain.global_explain import get_global_explanation
from app.explain.local_explain import get_local_explanation
from app.utils.file_handler import save_uploaded_file
from app.utils.data_loader import load_data

app = FastAPI()

DATA_PATH = "data.csv"
MODEL_PATH = "model.pkl"

# Request model for training
class TrainRequest(BaseModel):
    model_type: str
    target_column: str

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    save_uploaded_file(file, DATA_PATH)
    df = load_data(DATA_PATH)
    return {"columns": df.columns.tolist(), "rows": df.shape[0]}

@app.post("/train")
def train_endpoint(req: TrainRequest):
    return train_model(DATA_PATH, MODEL_PATH, req.model_type, req.target_column)

@app.get("/explain/global")
def global_explain():
    return get_global_explanation(DATA_PATH, MODEL_PATH)

@app.post("/explain/local")
def local_explain(index: int):
    return get_local_explanation(DATA_PATH, MODEL_PATH, index)
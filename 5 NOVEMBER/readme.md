# AI Explainability Backend

This FastAPI backend supports CSV upload, model training, and global/local model explanations using SHAP.

## Endpoints

- `POST /upload`: Upload CSV file
- `POST /train`: Train model (`model_type`, `target_column`)
- `GET /explain/global`: Global feature importance
- `POST /explain/local`: Local explanation for a row

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
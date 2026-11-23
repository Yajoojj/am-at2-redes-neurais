from contextlib import asynccontextmanager

import joblib
import pandas as pd
from fastapi import FastAPI

from src.schemas import Cliente, Resposta


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.modelo = joblib.load("models/modelo_mlp.joblib")
    yield


app = FastAPI(title="API Churn", lifespan=lifespan)


@app.get("/info")
def info():
    return {"status": "ativo", "framework": "FastAPI", "modelo": "MLPClassifier"}


@app.post("/predict", response_model=Resposta)
def predict(cliente: Cliente):
    df = pd.DataFrame([cliente.model_dump()])
    modelo = app.state.modelo

    classe = modelo.predict(df)[0]
    probabilidade = modelo.predict_proba(df)[0].max()

    return Resposta(classe_predita=classe, probabilidade=round(float(probabilidade), 4))

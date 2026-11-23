# AT2 - Redes Neurais MLP

Modelo MLP para prever churn (cancelamento) de clientes de telecom, com uma API em FastAPI.

Dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Video Demonstrando: https://youtu.be/ZgeRQpJTej0

## Como rodar

```
uv sync
uv run fastapi dev src/app.py
```

Swagger: http://127.0.0.1:8000/docs

Os testes estão no arquivo `requisicoes.http`.

O treino do modelo está em `notebooks/analise_treinamento.ipynb`.

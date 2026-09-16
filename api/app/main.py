from fastapi import FastAPI
from app.core.exception import registrar_handler
from app.controllers.usuario_controller import router as usuario_router


app = FastAPI()

# Traduz as excecoes de dominio (app/core/exception.py)  ara reespostas HTTP padronizadas
registrar_handler(app)

app.include_router(usuario_router)

# Executar
# uvicorn app.main:app --reload
# Chrome: localhost:8000/docs



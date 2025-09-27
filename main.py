import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import plantas_router



app = FastAPI()
app.include_router(plantas_router.router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


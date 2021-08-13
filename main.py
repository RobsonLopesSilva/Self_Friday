from fastapi import FastAPI
from pydantic import BaseModel
# comentarios

app = FastAPI()
@app.get('/')
def raiz():
    return{'Rock an Roll'}
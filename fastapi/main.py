from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/{name}')
async def root(name):
    return 'Hello, ' + name
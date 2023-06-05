from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
async def root(name):
    return 'Hello, ' + name
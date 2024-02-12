from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def list_products():
    return {'hello': 'world'}

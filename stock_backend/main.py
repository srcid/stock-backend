from fastapi import FastAPI

from stock_backend.scehemes import MessageScheme

app = FastAPI()


@app.get('/', status_code=200, response_model=MessageScheme)
async def read_root():
    return {'text': 'The quick fox jump over the lazy dog.'}

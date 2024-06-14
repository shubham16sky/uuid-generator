from fastapi import FastAPI
import uuid

app  = FastAPI()


@app.get('/')
async def root():
    return {'messsage':'Hey! It is up and working !'}

@app.get('/generate')
async def generate():
    _uuid = uuid.uuid1()
    return {'uuid':_uuid}



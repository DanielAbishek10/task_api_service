from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
async def home():
    return {"msg": 'hello'}


from fastapi import FastAPI
from app.user.route import router as globalrouter

app = FastAPI()

@app.get('/')
def user_info():
    return {"get started with" : "user authentic panel"}

app.include_router(globalrouter ,  prefix='/v1')


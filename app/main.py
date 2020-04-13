from fastapi import FastAPI
from app1.api import ping

app = FastAPI()
# @app.get("/ping")
# # def pong():
# #     return {"ping": "pong!"}
# async def pong():
#     # some async operation could happen here
#     return {"ping": "pong"}

app.include_router(ping.router)

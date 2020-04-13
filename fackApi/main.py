from fastapi import FastAPI
from fackApi import fakeDown
from fackApi import fakeUp

app = FastAPI()
app.include_router(fakeUp.router)
app.include_router(fakeDown.router)
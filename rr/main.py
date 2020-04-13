# 111111111111111111111111111

from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# 2222222222222222222
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None

# @app.get("/")
# def read_root():
#     return {"hello": "world"}

# 设置可选参数，q是可选的查询参数，默认值是None
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id":item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name":item.name, "item_id": item_id}

#333333333333333333333333333333
# from fastapi import FastAPI 

app = FastAPI()
@app.get("/")
async def main():
    return {"message": "Helloworld, FastAPI"}

# 444444444444444444444444444444 枚举
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet" 
    resnet = "resnet" 
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW"}
    if model_name.value ==  "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


#5555555555555555555  path转换器 starlette
@app.get("files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}

#666666666666 Query参数   声明不属于路径参数的其他函数参数时，它们将自动解释为Query参数，也就是查询参数
# query 就是一系列的在URL？之后的key-value键值对，每对键值对用&分割开来
# http://127.0.0.1:8000/items/?skip=0&limit=10 = http://127.0.0.2:8000/items/
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"},{"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# 77777777777777777query参数类型转换
# @app.get("/items/{item_id}")
# async def read_item(item_id: str,q:str = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update({
#             "description":"this is an amazing item that has a long description"
#         })
#     return item

# 8888888888888 同时使用Path参数 和Query 参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "this is an amazing item that has a long description"})
    return item

# 必需的查询参数   
@app.get("/items/{item_id}")
async def read_user_item(item_id:str, needy:str):
    item = {"item_id": item_id, "needy": needy}
    return item








if __name__ == '__main___':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

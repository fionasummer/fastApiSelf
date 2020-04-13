from pydantic import BaseModel
from fastapi import FastAPI

# 可以使用None让这个属性变为可选
# 创建数据模型  声明你的数据模型为一个类，且该类继承BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price : float
    tax : float = None

{
    "name" : "Foo",
    "description": "An optional descrition",
    "price": 45.2,
    "tax": 3.5
}

app = FastAPI()
# @app.post("/items/")
# async def create_item(item: Item):  # 声明参数的类型为创建的模型Item
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item
# 使用request body的好处，通过那样定义python类型为pydantic的model
# FastAPI 将会
# 将读取请求的正文读取为JSON类型
# 转换相应的类型
# 验证数据   （如果数据无效，他将返回一个清晰的错误，指出错误数据的确切位置和来源）
# 在参数item中为你提供接收的数据

# request body + path   同时定义path参数和请求体参数
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# Request body + path +query参数
# 同时定义path参数\Query参数\请求体参数
@app.put("/items/{items_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


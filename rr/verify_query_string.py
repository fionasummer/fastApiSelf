from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 为query参数附加验证
# from fastapi import FastAPI, Query
# app = FastAPI()
# @app.get("/items/")
# # 使用Query设置max_length验证， Query的第一个参数是定义默认值
# # 使用Query方法明确地将其声明为查询参数
# # 也可以添加min_length q: str=Query(None, min_length=m, max_length=n)
# async def read_items(q: str = Query(None, min_length=10, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 添加正则表达式验证
# q: str = Query(None, regex="regular expression")
# @app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery")):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 设置默认值
# @app.get("/items/")
# async def read_items(q: str = Query("fixedquery", min_length=3)):
#     results = {}
#     if q:
#         results.update({"q": q})
#     return results


# 使用query 声明该查询参数必需的时候，使用...作为第一个参数
# ... 它是一个特殊的单一值，这使FastAPI知道此参数是必需的
# @app.get("/items/")
# async def read_items(q: str = Query(..., min_length= 3)):
#     results = {}
#     if q:
#         results.update({"q": q})
#     return results

# 设置Query参数 列表/多个值
# 明确用Query定义查询参数的时候，声明该参数获取一个列表，或者说获取多个值
# 声明查询参数q 可以在URL中出现多次  q: List[str] = Query(None)
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/items/")
# http://localhost:8000/items/?q=foo&q=bar
# {"q": ["foo", "bar"]} 要声明类型为list的查询参数
# async def read_items(q: List[str] = Query(None)):
#     query_items = {"q": q}
#     return query_items

# query参数 列表、多个值设置默认值
# @app.get("/items/")
# async def read_items(q: List[str] = Query(["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items

# 使用list
# 直接使用list而不是list[str]
# FastAPI将不会检查列表中的内容 List[int]将会检查List里面元素是否都为整数，但是list本身并不会检查
# async def read_items(q: list = Query(None)):
#     query_items = {"q": q}
#     return query_items


# 声明更多元数据
async def read_items(q: str = Query(
    None,
    title="Query string",
    description=" query string for the items to search in the database",
    min_length=3
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results



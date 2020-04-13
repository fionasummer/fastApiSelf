from fastapi import FastAPI
# 跨域问题
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.core import config
from app.api.api_v1.api import api_router
from app.db.session import Session

app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

# CORS
origins = []

# set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(',')
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),

app.include_router(api_router, prefix=config.API_V1_STR)

# 创建中间件，中间件的功能，接受的request,函数call_next将接受request作为参数
# call_next 将传递request给相应的路径操作
# 然后它返回response由相应的path操作生成的
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


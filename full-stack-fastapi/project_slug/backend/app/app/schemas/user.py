from typing import Optional   # 这个参数可以为空或已经声明的类型
from pydantic import BaseModel, EmailStr


# 属性共享
class UserBase(BaseModel):
    email: Optional[EmailStr] = None


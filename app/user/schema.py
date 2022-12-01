from pydantic import BaseModel
from enum import Enum
from typing import Union

class Type(Enum):
    user_name = "user_name"
    email_id = "email_id"

class UserLoginData(BaseModel):
    type: Type
    user : str
    password : str

    class config:
        orm_mode = True

class UserSignupData(BaseModel):
    first_name : str
    last_name : str
    user_name : str
    email_id : str
    mobile_no : int
    password : str
    retype_password : str

    class Config:
        orm_mode = True

class ResetPasswordData(BaseModel):
    type : Type
    user : str

    class config:
        orm_mode = True





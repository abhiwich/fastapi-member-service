from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class MemberSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    mobile: str = Field(...)
    address: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Noomnim Ja",
                "email": "test@mail.com",
                "mobile": "0900000012",
                "address": "3/33 bangkok 10000",
            }
        }


class UpdateMemberModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    mobile: Optional[str]
    address: Optional[str]
    

    class Config:
        schema_extra = {
            "example": {
                 "fullname": "Noomnim Ja",
                "email": "test@mail.com",
                "mobile": "0900000012",
                "address": "3/33 bangkok 10000",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
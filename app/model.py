from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, Body, Depends
class UserSchema(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Indira",
                "email": "indira@gmail.com",
                "password": "admin"
            }
    }
        
class UserloginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "indira@gmail.com",
                "password": "admin"
            }
    }
        
class PostSchema(BaseModel):
    title: str= Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "cats",
                "description": "all about cats"
            }
    }
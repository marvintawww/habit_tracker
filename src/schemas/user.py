from pydantic import BaseModel, ConfigDict


class UserCreateData(BaseModel):
    login: str
    firstname: str
    lastname: str
    password: str


class UserCreateDB(BaseModel):
    login: str
    firstname: str
    lastname: str
    hashed_password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    firstname: str
    lastname: str

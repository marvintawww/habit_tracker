from pydantic import BaseModel, ConfigDict


class UserCreateData(BaseModel):
    login: str
    firstname: str
    lastname: str


class UserCreateDB(UserCreateData):
    pass


class UserCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    firstname: str
    lastname: str

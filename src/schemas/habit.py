from pydantic import BaseModel, ConfigDict


class HabitCreateData(BaseModel):
    title: str


class HabitCreateDB(BaseModel):
    title: str
    user_id: int


class HabitResponse(BaseModel):
    id: int
    title: str
    user_id: int

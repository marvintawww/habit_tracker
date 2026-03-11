from pydantic import BaseModel, ConfigDict


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class TokenPairResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    access_token: str
    refresh_token: str


class BlacklistedTokenDB(BaseModel):
    jti: str

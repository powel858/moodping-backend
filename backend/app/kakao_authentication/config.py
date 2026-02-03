from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class KakaoSettings(BaseSettings):
    client_id: str = Field(..., alias="KAKAO_CLIENT_ID")
    redirect_uri: str = Field(..., alias="KAKAO_REDIRECT_URI")
    client_secret: str | None = Field(None, alias="KAKAO_CLIENT_SECRET")
    
    # Kakao API Endpoints
    kakao_oauth_url: str = "https://kauth.kakao.com/oauth/authorize"
    kakao_token_url: str = "https://kauth.kakao.com/oauth/token"
    kakao_user_info_url: str = "https://kapi.kakao.com/v2/user/me"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_kakao_settings() -> KakaoSettings:
    return KakaoSettings()

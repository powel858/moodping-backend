from pydantic import BaseModel, Field

class KakaoOAuthUrlResponse(BaseModel):
    url: str = Field(..., description="The URL to redirect the user to for Kakao authentication")

class KakaoTokenResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str
    refresh_token_expires_in: int

class KakaoProfile(BaseModel):
    nickname: str
    thumbnail_image_url: str
    profile_image_url: str
    is_default_image: bool

class KakaoAccount(BaseModel):
    profile: KakaoProfile
    has_email: bool
    email: str
    is_email_valid: bool
    is_email_verified: bool

class KakaoUserInfoResponse(BaseModel):
    id: int
    connected_at: str
    kakao_account: KakaoAccount

class KakaoLoginResponse(BaseModel):
    token: KakaoTokenResponse
    user_info: KakaoUserInfoResponse

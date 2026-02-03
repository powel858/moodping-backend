from app.kakao_authentication.service.kakao_oauth_service import KakaoOauthService
from app.kakao_authentication.schemas import KakaoTokenResponse, KakaoUserInfoResponse
from app.kakao_authentication.config import KakaoSettings, get_kakao_settings
import httpx
from fastapi import HTTPException

class KakaoOauthServiceImpl(KakaoOauthService):
    def __init__(self):
        # We can inject settings here or load them. For simplicity in this structure
        # where we instantiate manually or via simple dependency, we use the cached settings.
        self.settings: KakaoSettings = get_kakao_settings()

    def get_kakao_login_link(self) -> str:
        return (
            f"{self.settings.kakao_oauth_url}?"
            f"client_id={self.settings.client_id}&"
            f"redirect_uri={self.settings.redirect_uri}&"
            f"response_type=code"
        )

    async def request_access_token(self, code: str) -> KakaoTokenResponse:
        payload = {
            "grant_type": "authorization_code",
            "client_id": self.settings.client_id,
            "redirect_uri": self.settings.redirect_uri,
            "code": code,
        }
        if self.settings.client_secret:
            payload["client_secret"] = self.settings.client_secret

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.settings.kakao_token_url, data=payload)
                response.raise_for_status()
                return KakaoTokenResponse(**response.json())
            except httpx.HTTPStatusError as e:
                error_details = e.response.text
                raise HTTPException(status_code=e.response.status_code, detail=f"Failed to request access token: {error_details}")
            except httpx.HTTPError as e:
                raise HTTPException(status_code=500, detail=f"Failed to request access token: {str(e)}")

    async def get_user_info(self, access_token: str) -> KakaoUserInfoResponse:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.settings.kakao_user_info_url, headers=headers)
                response.raise_for_status()
                return KakaoUserInfoResponse(**response.json())
            except httpx.HTTPError as e:
                raise HTTPException(status_code=500, detail=f"Failed to get user info: {str(e)}")

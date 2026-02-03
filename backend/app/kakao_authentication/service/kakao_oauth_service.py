from abc import ABC, abstractmethod
from app.kakao_authentication.schemas import KakaoTokenResponse, KakaoUserInfoResponse

class KakaoOauthService(ABC):
    @abstractmethod
    def get_kakao_login_link(self) -> str:
        """Generate Kakao OAuth login link."""
        pass

    @abstractmethod
    async def request_access_token(self, code: str) -> KakaoTokenResponse:
        """Request access token from Kakao."""
        pass

    @abstractmethod
    async def get_user_info(self, access_token: str) -> KakaoUserInfoResponse:
        """Get user info from Kakao."""
        pass

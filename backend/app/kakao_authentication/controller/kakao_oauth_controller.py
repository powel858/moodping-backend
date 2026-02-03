from fastapi import APIRouter, Depends, Query, HTTPException
from app.kakao_authentication.schemas import KakaoOAuthUrlResponse, KakaoLoginResponse
from app.kakao_authentication.service.kakao_oauth_service import KakaoOauthService
from app.kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl

router = APIRouter(prefix="/kakao-authentication", tags=["Kakao Authentication"])

# Dependency Injection factory
def get_kakao_oauth_service() -> KakaoOauthService:
    return KakaoOauthServiceImpl()

@router.get("/request-oauth-link", response_model=KakaoOAuthUrlResponse)
def request_oauth_link(
    service: KakaoOauthService = Depends(get_kakao_oauth_service)
):
    try:
        url = service.get_kakao_login_link()
        return KakaoOAuthUrlResponse(url=url)
    except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))

@router.get("/request-access-token-after-redirection", response_model=KakaoLoginResponse)
async def request_access_token(
    code: str = Query(..., description="Authorization code from Kakao"),
    service: KakaoOauthService = Depends(get_kakao_oauth_service)
):
    try:
        token_response = await service.request_access_token(code)
        user_info = await service.get_user_info(token_response.access_token)
        
        return KakaoLoginResponse(
            token=token_response,
            user_info=user_info
        )
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

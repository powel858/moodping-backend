import logging
from functools import lru_cache
from .base import BaseLLMClient
from moodping.config.settings import get_settings

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_llm_client() -> BaseLLMClient:
    provider = get_settings().llm_provider.lower().strip()
    logger.info("LLM 제공자: %s", provider)

    if provider == "openai":
        from .openai_client import OpenAIClient
        return OpenAIClient()
    elif provider == "gemini":
        from .gemini_client import GeminiClient
        return GeminiClient()
    elif provider == "claude":
        from .claude_client import ClaudeClient
        return ClaudeClient()
    else:
        raise ValueError(
            f"지원하지 않는 LLM_PROVIDER: '{provider}'. "
            f"openai | gemini | claude 중 하나를 선택하세요."
        )

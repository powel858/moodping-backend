#!/usr/bin/env python
"""Quick import test to check for import errors."""
import sys
import traceback

try:
    print("Testing imports...")
    from app.main import app
    print("✅ app.main imported successfully")
    from app.kakao_authentication.controller.kakao_authentication_controller import kakao_authentication_router
    print("✅ kakao_authentication_router imported successfully")
    from app.config import get_settings
    settings = get_settings()
    print(f"✅ Settings loaded: LLM_PROVIDER={settings.llm_provider}")
    print(f"✅ KAKAO_REDIRECT_URI={settings.kakao_redirect_uri}")
    print("\n✅ All imports successful! Server should work.")
except Exception as e:
    print(f"\n❌ Import error:")
    traceback.print_exc()
    sys.exit(1)

import httpx
import sys

def test_endpoints():
    base_url = "http://localhost:33333"
    
    # Test 1: Get OAuth Link
    try:
        print("Testing OAuth Link Generation...")
        resp = httpx.get(f"{base_url}/kakao-authentication/request-oauth-link")
        resp.raise_for_status()
        data = resp.json()
        print(f"Success: {data}")
        
        if "url" not in data:
            print("Error: 'url' field missing in response")
            sys.exit(1)
            
        print("Test 1 Passed")
    except Exception as e:
        print(f"Test 1 Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_endpoints()

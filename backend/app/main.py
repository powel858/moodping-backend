from fastapi import FastAPI
from app.config import env
from app.kakao_authentication.controller.kakao_oauth_controller import router as kakao_router

def create_app() -> FastAPI:
    # 1. Load Environment Variables
    env.load_env()

    # 2. Initialize FastAPI
    app = FastAPI()
    
    # 3. Include Routers
    app.include_router(kakao_router)

    return app

app = create_app()

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kakao Login Test</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #F7E600; /* Kakao Yellowish */
                margin: 0;
            }
            .container {
                text-align: center;
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            h1 { color: #3A1D1D; } /* Kakao Brown */
            button {
                background-color: #FEE500;
                color: #000000 85%;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                cursor: pointer;
                transition: transform 0.1s;
            }
            button:hover {
                transform: scale(1.05);
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>PM-EDDI Kakao Auth</h1>
            <p>Click below to start the authentication flow.</p>
            <button onclick="loginWithKakao()">Login with Kakao</button>
        </div>
        <script>
            async function loginWithKakao() {
                try {
                    const response = await fetch('/kakao-authentication/request-oauth-link');
                    const data = await response.json();
                    if (data.url) {
                        window.location.href = data.url;
                    } else {
                        alert('Failed to get Kakao URL');
                    }
                } catch (error) {
                    console.error('Error:', error);
                    alert('Error connecting to backend');
                }
            }
        </script>
    </body>
    </html>
    """

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import datetime

app = FastAPI()

# URL da imagem direta no Google
URL_DA_IMAGEM = "https://lh3.googleusercontent.com/d/1Xau3hnojurMNDQSHHFEuLcALrkrx-0D8"

@app.get("/")
def home():
    return {"status": "online", "message": "API de Redirecionamento ativa."}

@app.get("/view")
@app.get("/api/view")
@app.get("/{full_path:path}")
async def log_and_view(request: Request, full_path: str = ""):
    if full_path in ["", "docs", "openapi.json", "favicon.ico"]:
        if full_path == "":
            return home()
        return RedirectResponse(url="/docs")

    # Registo de logs na consola da Vercel
    user_agent = request.headers.get("user-agent", "Desconhecido")
    ip_origem = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
    if not ip_origem:
        ip_origem = request.headers.get("x-real-ip", "Desconhecido")
    data_hora = datetime.datetime.now(datetime.timezone.utc).isoformat()

    print(f"[{data_hora}] Leitura de QR Code | Rota: /{full_path} | IP: {ip_origem} | User-Agent: {user_agent}")

    # Retorna uma página HTML que ajusta a imagem a 100% da largura/altura do ecrã
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Imagem</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body, html {{
                width: 100%;
                height: 100%;
                background-color: #000;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }}
            img {{
                max-width: 100%;
                max-height: 100vh;
                object-fit: contain;
                width: auto;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <img src="{URL_DA_IMAGEM}" alt="Visualização">
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
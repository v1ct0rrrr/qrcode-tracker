from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import datetime

app = FastAPI()

# URL direto da img
URL_DA_IMAGEM = "https://lh3.googleusercontent.com/d/1Xau3hnojurMNDQSHHFEuLcALrkrx-0D8"

@app.get("/")
def home():
    return {"status": "online", "message": "API de Redirecionamento ativa."}

# Rota específica /view e rota genérica para apanhar qualquer variação (/api/view, /view/, etc.)
@app.get("/view")
@app.get("/api/view")
@app.get("/{full_path:path}")
async def log_and_redirect(request: Request, full_path: str = ""):
    # Se a requisição for para a raiz ou documentação, deixa o FastAPI responder normalmente
    if full_path in ["", "docs", "openapi.json", "favicon.ico"]:
        if full_path == "":
            return home()
        return RedirectResponse(url="/docs")

    # Registo de dados do dispositivo
    user_agent = request.headers.get("user-agent", "Desconhecido")
    
    ip_origem = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
    if not ip_origem:
        ip_origem = request.headers.get("x-real-ip", "Desconhecido")
        
    data_hora = datetime.datetime.now(datetime.timezone.utc).isoformat()

    print(f"[{data_hora}] Leitura de QR Code | Rota: /{full_path} | IP: {ip_origem} | User-Agent: {user_agent}")

    return RedirectResponse(url=URL_DA_IMAGEM, status_code=302)
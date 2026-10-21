from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import datetime

app = FastAPI()

# URL da imagem direta
URL_DA_IMAGEM = "https://lh3.googleusercontent.com/d/1lotyxfE5eqX4M5FAxIHy2wAw6jkhom_Z"

@app.get("/")
@app.get("/api")
def home():
    return {"status": "online", "message": "API de Redirecionamento ativa."}

# Aceita tanto /view quanto /api/view
@app.get("/view")
@app.get("/api/view")
async def log_and_redirect(request: Request):
    user_agent = request.headers.get("user-agent", "Desconhecido")
    
    ip_origem = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
    if not ip_origem:
        ip_origem = request.headers.get("x-real-ip", "Desconhecido")
        
    data_hora = datetime.datetime.now(datetime.timezone.utc).isoformat()

    print(f"[{data_hora}] Leitura de QR Code | IP: {ip_origem} | User-Agent: {user_agent}")

    return RedirectResponse(url=URL_DA_IMAGEM, status_code=302)
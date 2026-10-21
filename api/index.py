from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import datetime

app = FastAPI()

# Substitua pela URL direta da imagem que deseja exibir
URL_DA_IMAGEM = "https://lh3.googleusercontent.com/d/1lotyxfE5eqX4M5FAxIHy2wAw6jkhom_Z"

@app.get("/")
def home():
    return {"status": "online", "message": "API de Redirecionamento ativa."}

@app.get("/view")
async def log_and_redirect(request: Request):
    # Captura headers enviados pelo navegador
    user_agent = request.headers.get("user-agent", "Desconhecido")
    
    # Na Vercel, o IP real do cliente vem no header x-forwarded-for ou x-real-ip
    ip_origem = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
    if not ip_origem:
        ip_origem = request.headers.get("x-real-ip", "Desconhecido")
        
    data_hora = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Log visível em tempo real no Dashboard da Vercel (Runtime Logs)
    print(f"[{data_hora}] Leitura de QR Code | IP: {ip_origem} | User-Agent: {user_agent}")

    # HTTP 302: Redirecionamento temporário para o destino final
    return RedirectResponse(url=URL_DA_IMAGEM, status_code=302)
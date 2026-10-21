import qrcode

# URL pública do endpoint que você hospedou na nuvem
URL_PUBLICA = "https://meu-rastreador.vercel.app/view"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(URL_PUBLICA)
qr.make(fit=True)

# Gera e salva a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_final.png")
print("QR Code gerado com sucesso em 'qrcode_final.png'!")
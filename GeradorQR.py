import qrcode

# Substitua este texto pelo link ou documento hospedado(dica pessoal, criar um arquvivo no google drive)
qrcodeimg = "<link ou texto da qual irá usar>"

# Gera o QR Code
qr = qrcode.make(qrcodeimg)

# Salva como imagem o Qrcode na mesma pasta da qual esta armazenado o código
qr.save("qrcode_pdf.png")

print("QR Code gerado com sucesso!")

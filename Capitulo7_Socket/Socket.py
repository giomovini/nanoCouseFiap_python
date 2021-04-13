import socket
resp = "S"
while(resp == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url) # imprime o ip da URL passada pelo usuario
    print("O IP referente à url informada é: ", ip)
    resp = input("Digite <s> para continuar: ").upper()

resposta = input("Digite a sua resposta: ").upper()
while resposta == "SIM":
    nivel = input("Digite seu nivel de acesso, ADM(administração), USR(usuário), GUEST(visitante): ").upper()
    if nivel == "ADM" or nivel == "USR":
        genero = input("Digite seu gênero 'F'(Feminino) ou 'M'(masculino): ").upper()
        if nivel == "ADM":
            if genero == "F":
                print("Olá Administradora!")
            else:
                print("Olá administrador!")
        else:
            if genero == "F":
                print("Olá usuária!")
            else:
                print("Olá usuário!")
    elif nivel == "GUEST":
        print("Olá visitante!")
    else:
        print("Olá desconhecido(a)") 
resposta = input("Digite SIM para continuar: ").upper()
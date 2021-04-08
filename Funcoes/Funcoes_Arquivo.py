def chamarMenu():
    escolha = int(input("Digite: \n" 
    "<1> - Para Registrar ativos \n"
    "<2> - Para Persistir em arquivos \n"
    "<3> - Para Exibir ativos armazenados:\n "
    "Opção: "))
    return escolha

def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar: ").upper()

def persistir(dicionario):
    with open("3_3_ManipulaArquivos/inventario.csv", "a") as inv:
            for chave, valor in dicionario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" +valor[2]+"\n")
    return "Persistido com sucesso"

def exibir():
    with open("3_3_ManipulaArquivos/inventario.csv", "r") as inv:
            linhas = inv.readlines()
    return linhas

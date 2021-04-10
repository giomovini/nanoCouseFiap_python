import json
import os
if os.path.exists("3_3_ManipulaArquivos/inventario_json.json"):
    with open("3_3_ManipulaArquivos/inventario_json.json", "r") as arq_json:
        inventario = json.load(arq_json)
else:
    inventario = {}
opcao = int(input("Digite: "
                        "\n<1> - Para registrar ativos"
                        "\n<2> - Para exibir ativos armazenados"
                        "\nOpção: "))
while opcao > 0 and opcao < 3:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da ultima atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar: ").upper()
        with open("3_3_ManipulaArquivos/inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json) #.dump() => grava o dicionario no arquivo
        print("JSON gerado!!")  
    elif opcao == 2:
        with open("3_3_ManipulaArquivos/inventario_json.json", "r") as arq_json:
            resultado = json.load(arq_json)
            for chave, dado in inventario.items():
                print("Data.........: ", dado[0])
                print("Descrição....: ", dado[1])
                print("Departamento.: ", dado[2])
    opcao = int(input("Digite: "
                        "\n<1> - Para registrar ativos"
                        "\n<2> - Para exibir ativos armazenados"
                        "\nOpção: "))
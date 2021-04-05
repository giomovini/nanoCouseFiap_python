inventario = []
resposta = "S"

# adicionar item ao inventário
while resposta == "S":
    equipamento = [input("Equipamentos: "),
    float(input("Valor: ")),
    int(input("Número Serial: ")),
    input("Departamento: ")]

    # append -> cria novo elemento no array/lista
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

# exibir dado do inventário
for elemento in inventario:
    print("Nome............: ", elemento[0])
    print("Valor...........: ", elemento[1])
    print("Serial..........: ", elemento[2])
    print("Departamento....: ", elemento[3])

print("=================inventario=================")

# localizar um item do inventário
busca = input("Digite o nome do produto que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor...: ", elemento[1])
        print("Serial..: ", elemento[2])

# depreciar item do inventário
depreciacao = input("Digite o equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

# excluir item do inventário
serial = int(input("Digite o serial do equipamento que será excluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# exibir dados do inventário
for elemento in inventario: 
    print("Nome..........: ", elemento[0])
    print("Valor.........: ", elemento[1])
    print("Serial........: ", elemento[2])
    print("Departamento..: ", elemento[3])

# resumo de valores do inventário   
valores = []
for elemento in inventario:
    valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

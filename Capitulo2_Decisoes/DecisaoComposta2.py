nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade >= 65:
    print("O paciente", nome, "POSSUI atendimento prioritário!")
if idade < 65:
    print("O paciente", nome, "NÃO possui atendimento prioritário!")
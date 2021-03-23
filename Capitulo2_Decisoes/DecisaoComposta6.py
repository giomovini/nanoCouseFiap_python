nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa: ").lower()

# Primeiro problema a ser resolvido:
if doenca_infectocontagiosa == "sim":
    print("Encaminhe para a sala AMARELA")
elif doenca_infectocontagiosa == "não":
    print("Encaminhe para a sala BRANCA")
else: 
    print("Responda a suspeita de doença infectocontagiosa com 'sim' ou 'não'")

# Segundo problema a ser resolvido:
if idade >= 65: 
    print("Paciente COM prioridade")
else: 
    genero = input("Digite o gênero do paciente: ").lower()
    if genero == "feminino" and idade > 10:
        gravidez = input("A paciente está gravida? ").lower()
        if gravidez == "sim":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        Print("Paciente SEM prioridade")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").lower()

# Primeiro problema a ser resolvido:

while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NÃO":
    print("Digite SIM ou NÃO ")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa == "sim":
    print("Encaminhe para a sala AMARELA")
else:
    print("Encaminhe para a sala BRANCA")

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
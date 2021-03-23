nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doenca_infectocontagiosa = input(
    "Suspeita de doença infecto-contagiosa?, SIM ou NÃO: "
).upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será enviado para sala de espera AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será enviado para sala de espera AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NÃO":
    print("O paciente será enviado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NÃO":
    print("O paciente será enviadi para a sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infecto-contagiosa com SIM ou NÃO")
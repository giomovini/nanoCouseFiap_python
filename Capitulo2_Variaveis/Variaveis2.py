nome = input("Digite o seu nome: ")
faculdade = input("Qual faculdade você estuda? : ")
qntde_funcionarios = int(input("Quantos funcionários trabalhando nessa faculdade: "))
mediaMensalidade = float(input("Qual é a média da mensalidade: "))

print("Olá", nome, "você estuda na faculdade", faculdade)
print("Que possui", int(qntde_funcionarios), "funcionários.")
print("E a média de mensalidade da", faculdade, "é de", str(mediaMensalidade), "reais.")
print("===============Verifique os tipos de dados abaixos====================")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [faculdade] é: ", type(faculdade))
print("O tipo de dado da variável [qntd_funcionários] é: ", type(qntde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
with open("3_3_ManipulaArquivos/teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipos de dados da variavel: ", type(conteudo))
print("Conteudo do arquivo: ", conteudo)
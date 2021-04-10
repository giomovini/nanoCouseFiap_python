def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]

# dicionario -> onde se pretende pesquisar; chave -> dado que vai ser pesquisado


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:  # != -> diferente
        print("Nome..............: " + lista[0])
        print("Último acesso.....: " + lista[1])
        print("Última estação....: " + lista[2])


def excluir(dicionario, chave):
    # verifica se a chave(dado) existe
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......: ")
        print("Login: ", chave)
        print("Dados: ", valor)


def salvar(dicionario):
    with open("3_3_ManipulaArquivos/bancoDeDados.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + valor)
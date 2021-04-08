with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tao facil criar um arquivo.")

with open("teste.txt", "a") as arquivo:
    arquivo.write("Continuacao do texto")
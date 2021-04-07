# criando o dicionario de dados
usuarios = {}

usuarios = {
    "Chaves": ["Chaves Silva", "17/06/1975", "Recep_01"],
    "Quico": ["Enrico Flores", "03/06/1976", "Raiox_02"],
}

# pode ser escrito desta forma também:
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("##########==========##########")
print("Dados: ", usuarios.get("Chaves"))
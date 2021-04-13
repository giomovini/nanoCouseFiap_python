from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, São Paulo, SP'
print(Geocoder('AIzaSyAhdkEoRCAbzgsCG1pAM1pUGZ1zrYlinTM').geocode(endereco).coordinates)


# enderco = input("Digite um endereço com número e cidade. "
#                 "\nExemplo: Avenida Paulista, 100 São Paulo:\n")

# resultado = Geocoder.geocode(enderco)
# if resultado.valid_address == True:
#     print("Endereço completo...: ", resultado)
#     print("Coordenadas.........: ", resultado.coordinates)
#     print("Número..............: ", resultado.street_number)
#     print("CEP.................: ", resultado.postal_code)

# print("Foi (ram) encontrado(s) ", resultado.count, " endereço(s).")
# for r in resultado:
#     print("Cidade.........: ", r.state)
#     print("País...........: ", r.coutry)
#     print("Lougradouro....: ", r.route)
#     print("#############################")

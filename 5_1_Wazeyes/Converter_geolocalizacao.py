from pygeocoder import Geocoder
from Funcoes2_JSON import ler_arquivo, gravar_arquivo

dicionario = ler_arquivo("entrada.json")
lista =  dicionario["endereco"]

endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
# saida = ("coordenadas: ", Geocoder.geocode(endereco).coordinates)
# gravar_arquivo(saida, "saida.json")
import json
# Creacion de funciones a partir de archivos json
def cargar_paises_continentes():

    with open('json/country-by-continent.json') as file:
        lst_pais_continente = json.load(file)
        return lst_pais_continente

def cargar_moneda_pais():
    with open('json/country-by-currency-code.json') as file:
        lst_moneda_pais = json.load(file)
        return lst_moneda_pais


def cargar_idioma_pais():
    with open('json/country-by-languages.json') as file:
        lst_idioma_pais = json.load(file)
        return lst_idioma_pais


def cargar_poblacion_pais():
    with open('json/country-by-population.json') as file:
        lst_pais_poblacion = json.load(file)
        return lst_pais_poblacion


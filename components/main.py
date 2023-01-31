from clases import Continente
from clases import Pais
import json
from leer_json import *

def cargar_paises():
   
    with open('json/country-by-continent.json', 'r') as file:
        lst_paises_continente = json.load(file)
        print(lst_paises_continente)

    # continentes = {}

    # for lst_pais_continente in lst_paises_continente:
    #     nombre = lst_pais_continente['nombre']
    #     continente = lst_pais_continente['continente']
    #     idiomas = lst_pais_continente['idiomas']
    #     moneda = lst_pais_continente['moneda']
    #     poblacion = lst_pais_continente['poblacion']

    #     if continente not in continentes:
    #         continentes[continente] = Continente(continente)

    #     pais = Pais(nombre, continente, idiomas, moneda, poblacion)
    #     continentes[continente].agregar_pais(pais)

    #return continentes
   


# def obtener_mayor_poblacion(continentes):
#     mayor_poblacion = 0
#     nombre_continente = ''
#     for nombre, continente in continentes.items():
#         if continente.poblacion > mayor_poblacion:
#             mayor_poblacion = continente.poblacion
#             nombre_continente = nombre

#     return nombre_continente, mayor_poblacion

# def obtener_idioma_mas_hablado(continentes):
#     idiomas = {}
#     for nombre, continente in continentes.items():
#         for pais in continente.paises:
#             for idioma in pais.idiomas:
#                 if idioma not in idiomas:
#                     idiomas[idioma] = 0
#                 idiomas[idioma] += pais.poblacion / len(pais.idiomas)

#     idioma_mas_hablado = max(idiomas, key=idiomas.get)
#     return idioma_mas_hablado

# def obtener_moneda_mas_usada(continentes):
#     monedas = {}
#     for nombre, continente in continentes.items():
#         for pais in continente.paises:
#             if pais.moneda not in monedas:
#                 monedas[pais.moneda] = 0
#             monedas[pais.moneda] += 1

#     moneda_mas_usada = max


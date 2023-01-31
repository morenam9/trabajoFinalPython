from leer_json import *
import json
from collections import Counter

# Importo la clase Counter del módulo collections
# La lista que pasemos a Counter() sera el diccionario donde cada key corresponde a cada uno de los números de lista y cada value, a la cantidad de veces que se repite en ella.

# Clase Continente:

paises = cargar_paises_continentes()
idiomas = cargar_idioma_pais()
monedas = cargar_moneda_pais()
habitantes = cargar_poblacion_pais()


class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        if nombre == None:
            nombre == 1
        self.paises = []

    def get_paisesxContinente(self, paises):
        self.paises = paises

    
    # def set_pais(self, pais):
    #     self.paises.append(pais)

    # def get_poblacion(self):
    #     poblacion = 0
    #     for pais in self.paises:
    #         poblacion += pais.obtener_poblacion()
    #     return poblacion

# Clase País: 

class Pais(Continente):
    def __init__(self, nombre, idiomas, moneda, poblacion):
        self.nombre = nombre
        self.idiomas = idiomas
        self.moneda = moneda
        self.poblacion = poblacion


        # def get_idiomasxPaises(self, idiomas):
        #     self.pais = self.nombre
        

    # def get_idiomas(self):
    #     return self.idiomas

    # def get_moneda(self):
    #     return self.moneda

    # def get_poblacion(self):
    #     return self.poblacion


# Filtrar PAISES por CONTINENTES

listaEuropa = []
listaAmerica = []
listaAsia = []
listaOceania = []
listaAntarctica = []

# ------------------------------ Paises por Continente ------------------------------

for pais in paises:

    if pais["continent"] == "Europe":
        listaEuropa.append(pais)
    if pais["continent"] == "South America" or pais["continent"] == "North America":
        listaAmerica.append(pais)
    if pais["continent"] == "Asia":
        listaAsia.append(pais)
    if pais["continent"] == "Oceania":
        listaOceania.append(pais)
    if pais["continent"] == "Antarctica":
        listaAntarctica.append(pais)

# Recorre cada lista de continentes e imprime cada uno

# ----------------------- Europa -----------------------

# # print(listaEuropa)
# for europe in listaEuropa:
#     print(europe)                                                                                               

# ----------------------- America -----------------------

# # print(listaAmerica)
# for america in listaAmerica:
#     print(america)

# ----------------------- Asia -----------------------

# # print(listaAsia)
# for asia in listaAsia:
#     print(asia)

# ----------------------- Oceania -----------------------

# # print(listaOceania)
# for oceania in listaOceania:
#     print(oceania)

# ----------------------- Antartida -----------------------

# # print(listaAntarctica)
# for antarctica in listaAntarctica:
#     print(antarctica)

# ------------------------------ Idiomas por PAISES e IDIOMA mas hablado en TODO el mundo ------------------------------"

listaArrayIdiomasEuropa = []
listaArrayIdiomasAmerica = []
listaArrayIdiomasAsia = []
listaArrayIdiomasOceania = []
listaArrayIdiomasAntarctica = []

for idioma in idiomas:
    
    if idioma["country"] in [d["country"] for d in listaEuropa] :
        listaArrayIdiomasEuropa.append(idioma["languages"])
    
    if idioma["country"] in [d["country"] for d in listaAmerica] :
        listaArrayIdiomasAmerica.append(idioma["languages"])
    
    if idioma["country"] in [d["country"] for d in listaAsia] :
        listaArrayIdiomasAsia.append(idioma["languages"])
    
    if idioma["country"] in [d["country"] for d in listaOceania] :
        listaArrayIdiomasOceania.append(idioma["languages"])
    
    if idioma["country"] in [d["country"] for d in listaAntarctica] :
        listaArrayIdiomasAntarctica.append(idioma["languages"])

# print(listaArrayIdiomasEuropa)
# print(listaArrayIdiomasAmerica)
# print(listaArrayIdiomasAsia)
# print(listaArrayIdiomasOceania)
# print(listaArrayIdiomasAntarctica)

idiomasEuropa = []
idiomasAmerica = []
idiomasAsia = []
idiomasOceania = []
idiomasAntarctica = []
idiomasDelMundo = []

# ------------------------------ Idiomas Europa ------------------------------

for filaIdiomaEuropa in listaArrayIdiomasEuropa:
    for idioma in filaIdiomaEuropa:
        idiomasEuropa.append(idioma)
        idiomasDelMundo.append(idioma)
        
# print(Counter(idiomasEuropa))
print(f"El idioma que más se habla en Europa es el Alemán: %s" % Counter(idiomasEuropa).get('German'))

# ------------------------------ Idiomas America ------------------------------

for filaIdiomaAmerica in listaArrayIdiomasAmerica:
    for idioma in filaIdiomaAmerica:
        idiomasAmerica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAmerica))
print(f"El idioma que más se habla en América es el Español: %s" % Counter(idiomasAmerica).get('Spanish'))

# ------------------------------ Idiomas Asia ------------------------------

for filaIdiomaAsia in listaArrayIdiomasAsia:
    for idioma in filaIdiomaAsia:
        idiomasAsia.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAsia))
print(f"El idioma que más se habla en Asia es el Árabe: %s" % Counter(idiomasAsia).get('Arabic'))

# ------------------------------ Idiomas Oceania ------------------------------

for filaIdiomaOceania in listaArrayIdiomasOceania:
    for idioma in filaIdiomaOceania:
        idiomasOceania.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasOceania))
print(f"El idioma que más se habla en Oceania es el Inglés: %s" % Counter(idiomasOceania).get('English'))

# ------------------------------ Idiomas Antarctica ------------------------------

for filaIdiomaAntarctica in listaArrayIdiomasAntarctica:
    for idioma in filaIdiomaAntarctica:
        idiomasAntarctica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAntarctica))
print(f"El idioma que más se habla en la Antartida es el idioma Pingüino")

print(f"El idioma que más se habla en el Mundo es el Inglés: %s" % Counter(idiomasDelMundo).get('English'))


# ------------------------------ Monedas ------------------------------
# for moneda in monedas:
#     print(moneda)

# ------------------------------ Habitantes ------------------------------
# for habitante in habitantes:
#     print(habitante)
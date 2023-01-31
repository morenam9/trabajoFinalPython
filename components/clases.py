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
listaAfrica = []
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
    if pais["continent"] == "Africa":
        listaAfrica.append(pais)
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

# ----------------------- Africa -----------------------

# # print(listaAfrica)
# for africa in listaAfrica:
#     print(africa)

# ----------------------- Antartida -----------------------

# # print(listaAntarctica)
# for antarctica in listaAntarctica:
#     print(antarctica)


# ------------------------------ Habitantes ------------------------------

habitantesPaisesEuropa = []
habitantesPaisesAmerica = []
habitantesPaisesAsia = []
habitantesPaisesOceania = []
habitantesPaisesAfrica = []
habitantesPaisesAntarctica = []

for habitante in habitantes:
    if habitante["country"] in [d["country"] for d in listaEuropa] :
        habitantesPaisesEuropa.append(habitante["population"])
    if habitante["country"] in [d["country"] for d in listaAmerica] :
        habitantesPaisesAmerica.append(habitante["population"])
    if habitante["country"] in [d["country"] for d in listaAsia] :
        habitantesPaisesAsia.append(habitante["population"])
    if habitante["country"] in [d["country"] for d in listaOceania] :
        habitantesPaisesOceania.append(habitante["population"])
    if habitante["country"] in [d["country"] for d in listaAfrica] :
        habitantesPaisesAfrica.append(habitante["population"])
    if habitante["country"] in [d["country"] for d in listaAntarctica] :
        habitantesPaisesAntarctica.append(habitante["population"])

nroHabitantesEuropa = 0
nroHabitantesAmerica = 0
nroHabitantesAsia = 0
nroHabitantesOceania = 0
nroHabitantesAfrica = 0
nroHabitantesAntarctica= 0
continenteConMayorHabitantes = []

for nroHab in habitantesPaisesEuropa:
    nroHabitantesEuropa = nroHabitantesEuropa + nroHab
print(f"El continente Europeo tiene la siguiente cantidad de habitantes: %s" % nroHabitantesEuropa)


for nroHab in habitantesPaisesAmerica:
    nroHabitantesAmerica = nroHabitantesAmerica + nroHab
print(f"El continente Americano tiene la siguiente cantidad de habitantes: %s" % nroHabitantesAmerica)

for nroHab in habitantesPaisesAsia:
    nroHabitantesAsia = nroHabitantesAsia + nroHab
print(f"El continente de Asia tiene la siguiente cantidad de habitantes: %s" % nroHabitantesAsia)

for nroHab in habitantesPaisesOceania:
    nroHabitantesOceania = nroHabitantesOceania + nroHab
print(f"El continente de Oceania tiene la siguiente cantidad de habitantes: %s" % nroHabitantesOceania)

for nroHab in habitantesPaisesAfrica:
    nroHabitantesAfrica = nroHabitantesAfrica + nroHab
print(f"El continente Africano tiene la siguiente cantidad de habitantes: %s" % nroHabitantesAfrica)

for nroHab in habitantesPaisesAntarctica:
    nroHabitantesAntarctica = nroHabitantesAntarctica + nroHab
print(f"El continente de la Antartida tiene la siguiente cantidad de habitantes: %s" % nroHabitantesAntarctica)

continenteConMayorHabitantes.append([nroHabitantesEuropa, "Europa"])
continenteConMayorHabitantes.append([nroHabitantesAmerica, "America"])
continenteConMayorHabitantes.append([nroHabitantesAsia, "Asia"])
continenteConMayorHabitantes.append([nroHabitantesOceania, "Oceania"])
continenteConMayorHabitantes.append([nroHabitantesAfrica,"Africa"])
continenteConMayorHabitantes.append([nroHabitantesAntarctica, "Antartida"])
print(f"El continente con mayor poblacion es el Asiatico, con la siguiente cantidad de habitantes: %s" % max(continenteConMayorHabitantes))

# ------------------------------ Idiomas por PAISES e IDIOMA mas hablado en TODO el mundo ------------------------------"

listaArrayIdiomasEuropa = []
listaArrayIdiomasAmerica = []
listaArrayIdiomasAsia = []
listaArrayIdiomasOceania = []
listaArrayIdiomasAfrica = []
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
    
    if idioma["country"] in [d["country"] for d in listaAfrica] :
        listaArrayIdiomasAfrica.append(idioma["languages"])
    
    if idioma["country"] in [d["country"] for d in listaAntarctica] :
        listaArrayIdiomasAntarctica.append(idioma["languages"])

# print(listaArrayIdiomasEuropa)
# print(listaArrayIdiomasAmerica)
# print(listaArrayIdiomasAsia)
# print(listaArrayIdiomasOceania)
# print(listaArrayIdiomasAfrica)
# print(listaArrayIdiomasAntarctica)

idiomasEuropa = []
idiomasAmerica = []
idiomasAsia = []
idiomasOceania = []
idiomasAfrica = []
idiomasAntarctica = []
idiomasDelMundo = []

# ------------------------------ Idiomas Europa ------------------------------

for filaIdiomaEuropa in listaArrayIdiomasEuropa:
    for idioma in filaIdiomaEuropa:
        idiomasEuropa.append(idioma)
        idiomasDelMundo.append(idioma)
        
# print(Counter(idiomasEuropa))
print(f"El idioma que más se habla en Europa es el Alemán, los paises que lo hablan son en total: %s" % Counter(idiomasEuropa).get('German'))

# ------------------------------ Idiomas America ------------------------------

for filaIdiomaAmerica in listaArrayIdiomasAmerica:
    for idioma in filaIdiomaAmerica:
        idiomasAmerica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAmerica))
print(f"El idioma que más se habla en América es el Español, los paises que lo hablan son en total: %s" % Counter(idiomasAmerica).get('Spanish'))

# ------------------------------ Idiomas Asia ------------------------------

for filaIdiomaAsia in listaArrayIdiomasAsia:
    for idioma in filaIdiomaAsia:
        idiomasAsia.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAsia))
print(f"El idioma que más se habla en Asia es el Árabe, los paises que lo hablan son en total: %s" % Counter(idiomasAsia).get('Arabic'))

# ------------------------------ Idiomas Oceania ------------------------------

for filaIdiomaOceania in listaArrayIdiomasOceania:
    for idioma in filaIdiomaOceania:
        idiomasOceania.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasOceania))
print(f"El idioma que más se habla en Oceania es el Inglés, los paises que lo hablan son en total: %s" % Counter(idiomasOceania).get('English'))

# ------------------------------ Idiomas Africa ------------------------------

for filaIdiomaAfrica in listaArrayIdiomasAfrica:
    for idioma in filaIdiomaAfrica:
        idiomasAfrica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasOceania))
print(f"El idioma que más se habla en Africa es el Ful, los paises que lo hablan son en total: %s" % Counter(idiomasAfrica).get('Ful'))

# ------------------------------ Idiomas Antarctica ------------------------------

for filaIdiomaAntarctica in listaArrayIdiomasAntarctica:
    for idioma in filaIdiomaAntarctica:
        idiomasAntarctica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAntarctica))
print(f"El idioma que más se habla en la Antartida es el idioma Pingüino")

print(f"El idioma que más se habla en el Mundo es el Inglés, los paises que lo hablan son en total: %s" % Counter(idiomasDelMundo).get('English'))

# ------------------------------ Monedas ------------------------------

monedasEuropa = []
monedasAmerica = []
monedasAsia = []
monedasOceania = []
monedasAfrica = []
monedasAntarctica = []

for moneda in monedas:
    if moneda["country"] in [d["country"] for d in listaEuropa] :
        monedasEuropa.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in listaAmerica] :
        monedasAmerica.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in listaAsia] :
        monedasAsia.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in listaOceania] :
        monedasOceania.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in listaAfrica] :
        monedasAfrica.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in listaAntarctica] :
        monedasAntarctica.append(moneda["currency_code"])


# ------------------------------ Monedas Europa ------------------------------

        
# print(Counter(monedasEuropa))
print(f"La moneda que se usa en más paises de Europa es el EUR. Y la cantidad de paises que la usan es: %s" % Counter(monedasEuropa).get("EUR"))

# ------------------------------ Monedas America ------------------------------
# print(Counter(monedasAmerica))
print(f"La moneda que se usa en más paises de America es el XCD. Y la cantidad de paises que la usan es: %s" % Counter(monedasAmerica).get('XCD'))

# ------------------------------ Monedas Asia ------------------------------
# print(Counter(monedasAsia))
print(f"En Asia cada pais usa su propia moneda")

# ------------------------------ Monedas Oceania ------------------------------
# print(Counter(monedasOceania))
print(f"La moneda que se usa en más paises de Oceania es el USD. Y la cantidad de paises que la usan es: %s" % Counter(monedasOceania).get('USD'))

# ------------------------------ Monedas Africa ------------------------------
# print(Counter(monedasAfrica))
print(f"La moneda que se usa en más paises de Africa es el XOF. Y la cantidad de paises que la usan es: %s" % Counter(monedasAfrica).get('XOF'))

# ------------------------------ Monedas Antartida ------------------------------
# print(Counter(monedasAntarctica))
print(f"En la Antartida cada pais usa su propia moneda")


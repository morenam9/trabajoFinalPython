#El programa debe devolver como resultado la respuesta a las siguientes consultas:
#1- Qué continente tiene mayor población? y cuál es el número?
#2- Suponiendo que la población habla en proporciones iguales cada idioma del país. Qué idioma es el más hablado del mundo y cuál por cada continente?
#3- Qué moneda se usa en más países y cuántos países son?
from clases import Continente
from clases import Pais
from leer_json import *
import json

# Importo la clase Counter del modulo collections
# La lista que pasemos a Counter() sera el diccionario donde cada key corresponde a cada uno de los numeros de lista y cada value, a la cantidad de veces que se repite en ella.

# Importo las funciones que me traen los diccionarios con los datos de los paises.
paises = cargar_paises_continentes()
idiomas = cargar_idioma_pais()
monedas = cargar_moneda_pais()
habitantes = cargar_poblacion_pais()

# - Instancia objeto continente

obj_europa = Continente("Europe")
obj_n_america = Continente("North America")
obj_s_america = Continente("South America")
obj_asia = Continente("Asia")
obj_oceania = Continente("Oceania")
obj_africa = Continente("Africa")
obj_antarctica = Continente("Antarctica")
        
lst_obj_continentes = [obj_europa, obj_n_america, obj_s_america, obj_asia, obj_oceania, obj_africa, obj_antarctica]



# ------------------------------ Paises por Continente ------------------------------

for pais in paises:
    obj_pais = Pais(pais["country"])
    if pais["continent"] == "Europe":
        obj_europa.append_pais(obj_pais)
    if pais["continent"] == "North America":
        obj_n_america.append_pais(obj_pais)
    if pais["continent"] == "South America":
        obj_s_america.append_pais(obj_pais)
    if pais["continent"] == "Asia":
        obj_asia.append_pais(obj_pais)
    if pais["continent"] == "Oceania":
        obj_oceania.append_pais(obj_pais)
    if pais["continent"] == "Africa":
        obj_africa.append_pais(obj_pais)
    if pais["continent"] == "Antarctica":
        obj_antarctica.append_pais(obj_pais)


# ------------------------------ Habitantes ------------------------------
for habitante in habitantes:
    for obj_continente in lst_obj_continentes :
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises :
            nombre_pais = obj_pais.get_nombre_pais()
            if habitante["country"] == nombre_pais:
                obj_pais.set_habitantes(habitante["population"])

poblacionNAmerica = obj_n_america.get_poblacion()
poblacionSAmerica = obj_s_america.get_poblacion()
poblacionEuropa = obj_europa.get_poblacion()
nombreAsia = obj_asia.get_nombre_continente()
poblacionAsia = obj_asia.get_poblacion()
poblacionAfrica = obj_africa.get_poblacion()
poblacionOceania = obj_oceania.get_poblacion()
poblacionAntarctica = obj_antarctica.get_poblacion()

# ------------------------------ Monedas ------------------------------

for moneda in monedas:
    for obj_continente in lst_obj_continentes:
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises:
            nombre_pais = obj_pais.get_nombre_pais()
            if moneda["country"] == nombre_pais:
                obj_pais.set_monedas(moneda["currency_code"])

# ------------------------------ Idiomas ------------------------------

for idioma in idiomas:
    for obj_continente in lst_obj_continentes:
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises:
            nombre_pais = obj_pais.get_nombre_pais()
            if idioma["country"] == nombre_pais:
                obj_pais.set_idiomas(idioma["languages"])


idiomaNAmerica = obj_n_america.get_idioma()
idiomaSAmerica = obj_s_america.get_idioma()
idiomaEuropa = obj_europa.get_idioma()
idiomaAsia = obj_asia.get_idioma()
idiomaAfrica = obj_africa.get_idioma()
idiomaOceania = obj_oceania.get_idioma()
idiomaAntarctica = obj_antarctica.get_idioma()

idioma_mundo = Continente("").get_idiomaMundo()

monedaNAmerica = obj_n_america.get_moneda()
monedaSAmerica = obj_s_america.get_moneda()
monedaEuropa = obj_europa.get_moneda()
monedaAsia = obj_asia.get_moneda()
monedaAfrica = obj_africa.get_moneda()
monedaOceania = obj_oceania.get_moneda()
monedaAntarctica = obj_antarctica.get_moneda()

monedaMundo = Continente("").get_monedaMundo()

data = {
    "respuesta1": {
        "mayor_poblacion": nombreAsia,
        "numero": poblacionAsia
    },
    "respuesta2": {
        "idioma_mas_hablado": {
            "World": idioma_mundo,
            "Asia": idiomaAsia,
            "Africa": idiomaAfrica,
            "Europe": idiomaEuropa,
            "North America": idiomaNAmerica,
            "Antarctica": idiomaAntarctica,
            "Oceania": idiomaOceania,
            "South America": idiomaSAmerica,
        }
    },
    "respuesta3": {
        "moneda_mas_usada": "Falta obtener codigo moneda de EUR",
        "cant_paises": monedaMundo
    }
}

with open("respuestas.json", "w") as j:
    json.dump(data, j)
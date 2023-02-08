# Curso Básico de Python – Clase 10 – TP Final

# Importo todo lo que requiero para el programa: modulos, clases, etc.
from clases import Continente
from clases import Pais
from leer_json import *
from collections import Counter
import json

# Importo y asigno los diccionarios con informacion de paises y continentes a las respectivas variables.
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


# ------------------------------ Obtengo Paises por Continente ------------------------------

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


# ------------------------------ Obtengo Habitantes Por Paises ------------------------------
for habitante in habitantes:
    for obj_continente in lst_obj_continentes :
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises :
            nombre_pais = obj_pais.get_nombre_pais()
            if habitante["country"] == nombre_pais:
                obj_pais.set_habitantes(habitante["population"])


# - obtengo la poblacion por continente
poblacion_n_america = obj_n_america.get_poblacion()
poblacion_s_america = obj_s_america.get_poblacion()
poblacion_europa = obj_europa.get_poblacion()
poblacion_asia = obj_asia.get_poblacion()
poblacion_africa = obj_africa.get_poblacion()
poblacion_oceania = obj_oceania.get_poblacion()
poblacion_antarctica = obj_antarctica.get_poblacion()

# Obtengo nombre continente con mayor poblacion
nombre_asia = obj_asia.get_nombre_continente()

# ------------------------------ Monedas ------------------------------

for moneda in monedas:
    for obj_continente in lst_obj_continentes:
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises:
            nombre_pais = obj_pais.get_nombre_pais()
            if moneda["country"] == nombre_pais:
                obj_pais.set_monedas(moneda["currency_code"])

# - Instancia objeto continente para obtener las monedas por continente.
moneda_n_america = obj_n_america.get_moneda()
moneda_s_america = obj_s_america.get_moneda()
moneda_europa = obj_europa.get_moneda()
moneda_asia = obj_asia.get_moneda()
moneda_africa = obj_africa.get_moneda()
moneda_oceania = obj_oceania.get_moneda()
moneda_antarctica = obj_antarctica.get_moneda()


# listo las monedas por continente para obtener la que mas se utiliza por paises.

lst_moneda_mas_usada = [moneda_n_america, moneda_s_america, moneda_europa, moneda_asia, moneda_africa, moneda_oceania, moneda_antarctica]
moneda_mas_usada_mundo = []
for moneda in lst_moneda_mas_usada:
    for item in moneda:
        moneda_mas_usada_mundo.append(item)
conteo_moneda = Counter(moneda_mas_usada_mundo)
conteo_ordenado_moneda = dict(sorted(conteo_moneda.items(), key=lambda item:item[1], reverse=True))
moneda_mundo = next(iter(conteo_ordenado_moneda))
paises_usan_moneda = Counter(moneda_mas_usada_mundo).get(moneda_mundo)
# ------------------------------ Idiomas ------------------------------

for idioma in idiomas:
    for obj_continente in lst_obj_continentes:
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises:
            nombre_pais = obj_pais.get_nombre_pais()
            if idioma["country"] == nombre_pais:
                obj_pais.set_idiomas(idioma["languages"])

# - Instancia objeto continente para obtener los idiomas por continente.
idioma_n_america = obj_n_america.get_idioma()
idioma_s_america = obj_s_america.get_idioma()
idioma_europa = obj_europa.get_idioma()
idioma_asia = obj_asia.get_idioma()
idioma_africa = obj_africa.get_idioma()
idioma_oceania = obj_oceania.get_idioma()
idioma_antarctica = obj_antarctica.get_idioma()

# listo los idiomas por continente para obtener el que mas se habla  y luego retorno el mas hablado en todo el mundo.

idiomas_mas_hablados = [idioma_s_america, idioma_n_america, idioma_europa, idioma_asia, idioma_africa, idioma_oceania, idioma_antarctica]

conteo_idioma = Counter(idiomas_mas_hablados)

conteo_ordenado_idioma = dict(sorted(conteo_idioma.items(), key=lambda item:item[1],
reverse=True))

idioma_mundo = next(iter(conteo_ordenado_idioma))


# ------------------------------ Creacion de archivo JSON ------------------------------
data = {
    "respuesta1": {
        "mayor_poblacion": nombre_asia,
        "numero": poblacion_asia
    },
    "respuesta2": {
        "idioma_mas_hablado": {
            "World": idioma_mundo,
            "Asia": idioma_asia,
            "Africa": idioma_africa,
            "Europe": idioma_europa,
            "North America": idioma_n_america,
            "Antarctica": idioma_antarctica,
            "Oceania": idioma_oceania,
            "South America": idioma_s_america
        }
    },
    "respuesta3": {
        "moneda_mas_usada_por_paises": moneda_mundo,
        "cantidad_de_paises": paises_usan_moneda
    }
}

with open("respuestas.json", "w") as j:
    json.dump(data, j)
#El programa debe devolver como resultado la respuesta a las siguientes consultas:
#1- Qué continente tiene mayor población? y cuál es el número?
#2- Suponiendo que la población habla en proporciones iguales cada idioma del país. Qué idioma es el más hablado del mundo y cuál por cada continente?
#3- Qué moneda se usa en más países y cuántos países son?


from leer_json import *
from collections import Counter

# Importo la clase Counter del modulo collections
# La lista que pasemos a Counter() sera el diccionario donde cada key corresponde a cada uno de los numeros de lista y cada value, a la cantidad de veces que se repite en ella.

# Importo las funciones que me traen los diccionarios con los datos de los paises.
paises = cargar_paises_continentes()
idiomas = cargar_idioma_pais()
monedas = cargar_moneda_pais()
habitantes = cargar_poblacion_pais()

# Clase Continente:

class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        if nombre == None:
            self.nombre = "Pais Invalido"
        self.paises = []

    def get_nombre (self):
        return self.nombre

    def get_paises(self, paises):
        return self.paises

    def append_pais(self, pais):
        self.paises.append(pais)

    def get_poblacion(self):
        poblacion = 0
        for pais in self.paises:
            poblacion += pais.obtener_poblacion()
        return poblacion

# Clase Pais:

class Pais():
    def __init__(self, nombre):
        self.nombre = nombre
        self.idiomas = []
        self.moneda = None
        self.poblacion = 0

        def set_habitantes(self, habitantes):
            self.poblacion = habitantes

        def get_nombre(self):
            return self.nombre

        def get_idiomas(self):
            return self.idiomas

        def get_moneda(self):
            return self.moneda

        def get_habitantes(self):
            return self.habitantes


# Filtrar PAISES por CONTINENTES - YA NO VA
# listaEuropa = []
# listaAmerica = []
# listaAsia = []
# listaOceania = []
# listaAfrica = []
# listaAntarctica = []



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
        obj_europa.append(obj_pais)
    if pais["continent"] == "North America":
        obj_n_america.append(pais)
    if pais["continent"] == "South America":
        obj_s_america.append(pais)
    if pais["continent"] == "Asia":
        obj_asia.append(pais)
    if pais["continent"] == "Oceania":
        obj_oceania.append(pais)
    if pais["continent"] == "Africa":
        obj_africa.append(pais)
    if pais["continent"] == "Antarctica":
        obj_antarctica.append(pais)



# ------------------------------ Habitantes ------------------------------
for habitante in habitantes:
    for obj_continente in lst_obj_continentes :
        lst_obj_paises = obj_continente.get_paises()
        for obj_pais in lst_obj_paises :
            nombre_pais = obj_pais.get_nombre()
            if habitante["country"] == nombre_pais:
                obj_pais.set_habitantes(habitante["population"])


# habitantesPaisesEuropa = []
# habitantesPaisesAmerica = []
# habitantesPaisesAsia = []
# habitantesPaisesOceania = []
# habitantesPaisesAfrica = []
# habitantesPaisesAntarctica = []

# for habitante in habitantes:
#     if habitante["country"] in [d["country"] for d in obj_europa] :
#         habitantesPaisesEuropa.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_n_america] :
#         habitantesPaisesAmerica.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_s_america] :
#         habitantesPaisesAmerica.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_asia] :
#         habitantesPaisesAsia.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_oceania] :
#         habitantesPaisesOceania.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_africa] :
#         habitantesPaisesAfrica.append(habitante["population"])
#     if habitante["country"] in [d["country"] for d in obj_antarctica] :
#         habitantesPaisesAntarctica.append(habitante["population"])

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

    if idioma["country"] in [d["country"] for d in obj_europa] :
        listaArrayIdiomasEuropa.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_n_america] :
        listaArrayIdiomasAmerica.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_s_america] :
        listaArrayIdiomasAmerica.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_asia] :
        listaArrayIdiomasAsia.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_oceania] :
        listaArrayIdiomasOceania.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_africa] :
        listaArrayIdiomasAfrica.append(idioma["languages"])

    if idioma["country"] in [d["country"] for d in obj_antarctica] :
        listaArrayIdiomasAntarctica.append(idioma["languages"])


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

print(f"El idioma que mas se habla en Europa es el Aleman, los paises que lo hablan son en total: %s" % Counter(idiomasEuropa).get('German'))

# ------------------------------ Idiomas America ------------------------------

for filaIdiomaAmerica in listaArrayIdiomasAmerica:
    for idioma in filaIdiomaAmerica:
        idiomasAmerica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAmerica))
print(f"El idioma que mas se habla en America es el Español, los paises que lo hablan son en total: %s" % Counter(idiomasAmerica).get('Spanish'))

# ------------------------------ Idiomas Asia ------------------------------

for filaIdiomaAsia in listaArrayIdiomasAsia:
    for idioma in filaIdiomaAsia:
        idiomasAsia.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAsia))
print(f"El idioma que mas se habla en Asia es el arabe, los paises que lo hablan son en total: %s" % Counter(idiomasAsia).get('Arabic'))

# ------------------------------ Idiomas Oceania ------------------------------

for filaIdiomaOceania in listaArrayIdiomasOceania:
    for idioma in filaIdiomaOceania:
        idiomasOceania.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasOceania))
print(f"El idioma que mas se habla en Oceania es el Ingles, los paises que lo hablan son en total: %s" % Counter(idiomasOceania).get('English'))

# ------------------------------ Idiomas Africa ------------------------------

for filaIdiomaAfrica in listaArrayIdiomasAfrica:
    for idioma in filaIdiomaAfrica:
        idiomasAfrica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasOceania))
print(f"El idioma que mas se habla en Africa es el Ful, los paises que lo hablan son en total: %s" % Counter(idiomasAfrica).get('Ful'))

# ------------------------------ Idiomas Antarctica ------------------------------

for filaIdiomaAntarctica in listaArrayIdiomasAntarctica:
    for idioma in filaIdiomaAntarctica:
        idiomasAntarctica.append(idioma)
        idiomasDelMundo.append(idioma)

# print(Counter(idiomasAntarctica))
print(f"El idioma que mas se habla en la Antartida es el idioma Pingüino")

print(f"El idioma que mas se habla en el Mundo es el Ingles, los paises que lo hablan son en total: %s" % Counter(idiomasDelMundo).get('English'))

# ------------------------------ Monedas ------------------------------

monedasEuropa = []
monedasAmerica = []
monedasAsia = []
monedasOceania = []
monedasAfrica = []
monedasAntarctica = []

for moneda in monedas:
    if moneda["country"] in [d["country"] for d in obj_europa] :
        monedasEuropa.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_n_america] :
        monedasAmerica.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_s_america] :
        monedasAmerica.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_asia] :
        monedasAsia.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_oceania] :
        monedasOceania.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_africa]:
        monedasAfrica.append(moneda["currency_code"])
    if moneda["country"] in [d["country"] for d in obj_antarctica] :
        monedasAntarctica.append(moneda["currency_code"])


# ------------------------------ Monedas Europa ------------------------------


print(f"La moneda que se usa en mas paises de Europa es el EUR. Y la cantidad de paises que la usan es: %s" % Counter(monedasEuropa).get("EUR"))

# ------------------------------ Monedas America ------------------------------

print(f"La moneda que se usa en mas paises de America es el XCD. Y la cantidad de paises que la usan es: %s" % Counter(monedasAmerica).get('XCD'))

# ------------------------------ Monedas Asia ------------------------------
# print(Counter(monedasAsia))
print(f"En Asia cada pais usa su propia moneda")

# ------------------------------ Monedas Oceania ------------------------------
# print(Counter(monedasOceania))
print(f"La moneda que se usa en mas paises de Oceania es el USD. Y la cantidad de paises que la usan es: %s" % Counter(monedasOceania).get('USD'))

# ------------------------------ Monedas Africa ------------------------------
# print(Counter(monedasAfrica))
print(f"La moneda que se usa en mas paises de Africa es el XOF. Y la cantidad de paises que la usan es: %s" % Counter(monedasAfrica).get('XOF'))

# ------------------------------ Monedas Antartida ------------------------------
# print(Counter(monedasAntarctica))
print(f"En la Antartida cada pais usa su propia moneda")


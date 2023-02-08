#Imports
from collections import Counter

# Clase Continente:

class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        if nombre == None:
            self.nombre = "Pais Invalido"
        self.paises = []
        self.poblacion = []
        self.idioma = []
        self.moneda = []


    def get_nombre_continente(self):
        return self.nombre

    def get_paises(self):
        return self.paises

    def append_pais(self, pais):
        self.paises.append(pais)

    def get_poblacion(self):
        self.poblacion = 0
        for pais in self.paises:
            self.poblacion += pais.poblacion
        return self.poblacion


    def get_idioma(self):
        idiomas = []
        for pais in self.paises:
            for idioma in pais.idiomas:
                for item in idioma:
                    idiomas.append(item)
        self.idioma.append(Counter(idiomas))
        idioma_mas_hablado_continente = "No posee idioma oficial"
        paises_max = 0
        for item_idioma in self.idioma:
            for idioma, paises in item_idioma.items():
                if paises > paises_max :
                    idioma_mas_hablado_continente = idioma
                    paises_max = paises
        self.idioma.append(idioma_mas_hablado_continente)
        return idioma_mas_hablado_continente

    def get_moneda(self):
        monedas = []
        for pais in self.paises:
            monedas.append(pais.moneda)
        return monedas

# Clase Pais:

class Pais:
    def __init__(self, nombre):
        self.nombre = nombre
        self.idiomas = []
        self.moneda = None
        self.poblacion = 0

    def get_nombre_pais(self):
        return self.nombre

    def get_habitantes(self):
        return self.poblacion

    def get_idiomas(self):
        return self.idiomas

    def get_moneda(self):
        return self.moneda

    def set_habitantes(self, habitantes):
        self.poblacion += habitantes

    def set_monedas(self, divisa):
        self.moneda = divisa

    def set_idiomas(self, idioma):
        self.idiomas.append(idioma)

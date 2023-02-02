# Clase Continente:

class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        if nombre == None:
            self.nombre = "Pais Invalido"
        self.paises = []

    def get_nombre_continente(self):
        return self.nombre

    def get_paises(self):
        return self.paises

    def append_pais(self, pais):
        self.paises.append(pais)

    def get_poblacion(self):
        poblacion = 0
        for pais in self.paises:
            poblacion += pais.get_poblacion()
        return poblacion

# Clase Pais:

class Pais():
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
        self.poblacion = habitantes

    def set_monedas(self, divisa):
        self.moneda = divisa
    
    def set_idiomas(self, idioma):
        self.idiomas.append(idioma)

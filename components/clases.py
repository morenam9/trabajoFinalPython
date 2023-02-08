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
    idiomaMasHabladoMundo = []
    monedaMundo = []

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
        self.idiomaMasHabladoMundo.append(idiomas)
        idioma_mas_hablado_continente = "Ninguno"
        paises_max = 0
        for itemIdioma in self.idioma:
            for idioma, paises in itemIdioma.items():
                if paises > paises_max :
                    idioma_mas_hablado_continente = idioma
                    paises_max = paises 
        self.idioma.append(idioma_mas_hablado_continente)
        return idioma_mas_hablado_continente

    def get_idiomaMundo(self):
        idiomaMundo = []
        for item in self.idiomaMasHabladoMundo:
            for item2 in item:
                idiomaMundo.append(item2)
        mensaje = f"El idioma que mas se habla en el Mundo es el Ingles, los paises que lo hablan son en total: %s" % Counter(idiomaMundo).get('English')
        return mensaje
    
    def get_moneda(self):
        monedas = []
        for pais in self.paises:
            monedas.append(pais.moneda)
        self.moneda.append(Counter(monedas))
        self.monedaMundo.append(monedas)
        moneda_mas_usada = "Ninguna"
        paises_max = 0
        for itemMoneda in self.moneda:
            for moneda, paises in itemMoneda.items():
                if paises > paises_max:
                    moneda_mas_usada = moneda
                    paises_max = paises
        self.moneda.append(moneda_mas_usada)
        mensaje = f"La moneda que mas se usa en %s " % self.get_nombre_continente()
        mensaje2 = f"es: %s" % moneda_mas_usada
        mensaje3 = f", los paises que lo usan son en total: %s" % Counter(monedas).get(moneda_mas_usada)
        return mensaje + mensaje2 + mensaje3
    
    def get_monedaMundo(self):
        monedaMundo = []
        for item in self.monedaMundo:
            for item2 in item:
                monedaMundo.append(item2)
        mensaje = Counter(monedaMundo).get('EUR')
        return mensaje

    



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

    
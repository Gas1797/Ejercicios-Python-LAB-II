class Paciente:

    def __init__(self,nombre="",edad="0",dni="0",genero="",peso="0",altura="0"):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.genero = genero
        self.peso = peso
        self.altura = altura
#comienzo Set atributos
    def setNombre(self,nombre):
        self.nombre = nombre
    def setEdad(self,edad):
        self.edad = edad
    def setDni(self,dni):
        self.dni = dni
    def setGenero(self,genero):
        self.genero = genero
    def setPeso(self,peso):
        self.peso = peso
    def setAltura(self,altura):
        self.altura = altura
#Comienzo Get Atributos
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getDni(self):
        return self.dni
    def getGenero(self):
        return self.genero
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura
    
    def esMayor(self):
        return int(self.getEdad()) >= 18
    
class Persona:
    def __init__(self, nombre="", edad=0, correo=""):
        self.nombre=nombre
        self.edad=edad
        self.correo=correo

    def setNombre(self,nombre):
        self.nombre=nombre
    def setEdad(self,edad):
        self.edad=edad
    def setCorreo(self,correo):
        self.correo=correo

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getCorreo(self):
        return self.correo

    def __str__(self):
        return self.nombre + " " + self.correo

    def isJoven(self):
        return self.getEdad() < 18

    def isJovenAdulto(self):
        return self.getEdad() >= 18 and self.getEdad() < 30
from Model.Persona import Persona
from Vista.VistaPersona import VistaPersona

class ControllerPersona:
    def __init__(self, vista = VistaPersona(),persona=Persona()):
        self.vista = vista
        self.persona = persona
        self.listaObjetoPersona=[]

    def pedirTipoMensaje(self):
        return self.vista.pedirTipoMensaje()

    def escribirArchivo(self,lista):
        with open("lista_correos.txt", "w") as archivo2:
            for l in lista:
                archivo2.write(str(l))
        self.vista.imprimir(lista)

    def tomarDatos(self):
        with open("personas.txt", "r") as archivo:
            for linea in archivo:
                vec = linea.split(",")
                self.listaObjetoPersona.append(Persona(vec[0],int(vec[1]),vec[2]))

    def consultarFiltrosPublicidad(self,mensaje):
        listacorreo=[]
        for p in self.listaObjetoPersona:
            if p.isJoven() and mensaje == 1:
                listacorreo.append(p.getCorreo())
            if p.isJovenAdulto() and mensaje == 2:
                listacorreo.append(p.getCorreo())
            if p.getEdad() >= 30 and mensaje == 3:
                listacorreo.append(p.getCorreo())
        self.escribirArchivo(listacorreo)

    
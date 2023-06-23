from Model.Paciente import Paciente
from Vista.VistaPaciente import VistaPaciente

class controllerPaciente:
    def __init__(self,vista=VistaPaciente(),paciente=Paciente()):

        self.paciente=paciente
        self.vista=vista
        self.listaPacientes=[]
        self.listaPacientes2=[]

    def bienvenida(self):
        return self.vista.bienvenida()

    def llenarlista1(self):
        with open("pacientes.txt", "r") as archivo:
            for linea in archivo:
                vec = linea.split(";")
                self.listaPacientes.append(Paciente(vec[0],(vec[1]),vec[2],vec[3],vec[4],vec[5]))
        
    def mostrarlista(self):
        lista=[]
        for pac in self.listaPacientes:
            lista.append(pac.getNombre())
            lista.append(pac.getDni())
        return self.vista.mostrarArchivoPacientes(lista)
    
#METODO PRINCIPAL
    def ejecutar(self,opcion):
        if opcion==1:
            self.mayoresEdad()
        elif opcion==2:
            pacienteElegido = self.vista.seleccionarPaciente()
            peso_nuevo = int(self.seleccionarPaciente(pacienteElegido))
            self.pesoIdeal(peso_nuevo)
            self.diferenciaPeso(peso_nuevo)
    
    def mayoresEdad(self):#opcion1
        for p in self.listaPacientes:
                if p.esMayor():
                    self.listaPacientes2.append(p.getNombre())
        print("La lista de pacientes mayores es: \n")
        print(self.listaPacientes2)

                 
            
    def seleccionarPaciente(self,pacienteElegido):#OPCION 2
        #pacienteElegido = int(self.seleccionarPaciente())
        for paciente in self.listaPacientes:
            if int(pacienteElegido) == int(paciente.getDni()):
                self.paciente = paciente
                return input(" <- Ingrese el peso nuevo a registrar\n") #PESO NUEVO
            else:
                print("No se ha encontrado el paciente: ",pacienteElegido)

    def pesoIdeal(self,peso_nuevo):
        formula = float(self.paciente.getAltura())**2
        #
        calculo = peso_nuevo / (formula)
        if calculo < 20:
            print("El paciente esta en su peso ideal\n")
        elif calculo >=20 and calculo<=25:
            print("El paciente esta por debajo de su peso ideal\n")
        elif calculo > 25:
            print("El paciente tiene sobrepeso\n")

    def diferenciaPeso(self,peso_nuevo):
        pesoviejo = int(self.paciente.getPeso())
        if peso_nuevo > pesoviejo:
            print("El peso del paciente ha aumentado\n")
        elif peso_nuevo == pesoviejo:
            print("El peso del paciente permanece igual\n")
        else:
            print("El peso del paciente ha disminuido\n")




            

    
    

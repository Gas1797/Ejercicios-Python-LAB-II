class VistaPaciente:
    def bienvenida(self):
        return int(input("\nIngrese la opcion: \n 1-Consultar Pacientes Mayor de edad \n 2-Registrar Peso\n"))
    
    def mostrarArchivoPacientes(self,lista):
        print("La lista de pacientes actual es:")
        print(lista)


    def seleccionarPaciente(self):
        return int(input("Seleccione un paciente ingresando su DNI para registrar un nuevo peso\n"))



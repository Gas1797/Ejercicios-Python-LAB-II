from Controller.ControllerPaciente import controllerPaciente

if __name__ == '__main__':
    controlador = controllerPaciente()

    try:
        opcion = controlador.bienvenida()
        controlador.llenarlista1()
        controlador.mostrarlista()
        controlador.ejecutar(opcion)
        
    except ValueError:
        print("no selecciono correctamente")

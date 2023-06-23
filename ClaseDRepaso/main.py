from Controller.ControllerPersona import ControllerPersona

if __name__ == '__main__':
    controlador = ControllerPersona()
    try:
        mensaje = controlador.pedirTipoMensaje()
        try:
            controlador.tomarDatos()
            controlador.consultarFiltrosPublicidad(mensaje)
        except FileNotFoundError:
            print ("NO esta el archivo")
    except ValueError:
        print("No ingreso el dato correcto")

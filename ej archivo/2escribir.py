lista = []
print(" ")
cantidad = int(input("Ingrese la cantidad de alumnos"))
with open("alumnos.txt", "a") as archivo:
    for i in range(cantidad):
        if i !=0:
            archivo.write("\n")
        for d in range(4):
            datos=input("ingrese datos")
            archivo.write(datos + ",")

def escribirlineas():#escribir lineas desde un array
    with open("alumnos.txt", "a") as archivo:
        archivo.writelines(["\n Linea 1" , "\n Linea 2" , "\n Linea3"])

#leer + escribir = "w+"
#leer + agregar = "a+"
#leer + escribir = "r+"

#Excepciones mas comunes: FileNotFoundError (no existe)  // PermissionError (no se puede acceder) // IsADirectoryError (es un directorio)

def eliminararchivo():
    import os
    os.remove(archivo)

def directorioactual():
    import os
    print(os.getcwd())
    

    


   
   
            
        



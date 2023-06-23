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


    


   
   
            
        



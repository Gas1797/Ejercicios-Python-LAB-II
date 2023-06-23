import re
numeros = open("numtelefonicos.txt", "r")
palabra = "353"
lineaelegida = numeros.readlines()
print(str("Nombres Telefonos"))
with open("numtelefonicos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.rstrip("\n").replace(";"," "))


with open("numtelefonicos.txt", "r") as archivo:
    for linea in archivo:
        dato = linea.split(";")
        print(dato)

print("PRUEBA \n")
with open("../numtelefonicos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.rstrip("\n").replace(";"," "))

print("\n prueba2")
lista=[]
with open("numtelefonicos.txt", "r") as archivo:
    for linea in archivo:
        lista.append(linea.split(";"))
        #lista = [linea.rstrip() for linea in archivo]
        #lista = list(map(str.rstrip, archivo))
    print(lista)



print("\n")


#diccionarios:

diccionario = {"azul":"blue" , "rojo":"red" , "amarillo":"yellow"}
#agregar:
diccionario["verde"] = "green"
#modificar:
diccionario["azul"] = "BLUE"
#borrar
del(diccionario["amarillo"])
#agregar lista en el diccionario:
diccionario2 = {"Gabriel":[1.70 , 25] , "Juan" : [1.89 , 30]}
#agregar diccionarios en diccionarios:
diccionario3 = {"Gabriel":{"estatura":1.70 , "edad":25 } , "Juan" : {"estatura":1.89 , "edad":30 } }
#print:
print(diccionario["azul"])
print(diccionario3["Gabriel"])
#buscar en diccionario:
print("azul" in diccionario)
#otra manera de buscar con get:
print(diccionario.get("azul","no existe esa clave"))
#mostrar solo claves:
print(diccionario.keys())
#mostrar solo valores:
print(diccionario.values())
#mostrar ambos sin usar print(diccionario):
print(diccionario.items())
#longitud
print(len(diccionario))
#limpiar todo el diccionario
diccionario.clear()
print(diccionario)





#


#with open("numtelefonicos.txt", "r") as archivo:
#    for linea in archivo:
#        buscar = re.search(palabra,linea)
#    if buscar==True:
#        print("La palabra fue encontrada")


        
    


        


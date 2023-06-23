#escribir una funcion que pida un numero entero entre 1 y 10 y guarde en un fichero "tabla-n.txt" la tabla de 
#multiplicar de ese numero donde n es introducido por usuario

#def ej1():
#    n=int(input("introduce numero"))
#    nombre_fichero = 'tabla-' + str(n) + '.txt'
#    file = open(nombre_fichero, "w")
#    for i in range (1,11):
#        file.write(str(n) + ' x ' + str(i) ' = ' + str(n*i) + '\n')
#    file.close


#funcion que pida dos numeros "n" y "m" entre 1 y 10 lea el fichero tabla, con la tabla de multiplicar de ese numero
# y muestre por pantalla la linea m, mostrar si no existe el fichero

def ej2():
    n=int(input("introduce numero"))
    m=int(input("introduce numero m"))
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    try:
        with open(nombre_fichero,"r") as file:
            lineas = file.readlines()
        print(lineas[m - 1])
    except FileNotFoundError:
        print("El fichero de la tabla del " ,n," no existe")

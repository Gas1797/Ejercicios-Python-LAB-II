import os
print("\n")
numeros = open("numtelefonicos.txt", "r")
for line in numeros.readlines():
    print (line)

print(os.listdir("."))
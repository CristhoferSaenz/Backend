#bucles es una estructura de control que permite repetir un bloque de código varias veces

##for
paises = ["Argentina", "Brasil", "Chile", "Uruguay","Brasil"] # crea una lista de paises

for pais in paises: # recorre la lista de paises y asigna cada elemento a la variable pais
    print(pais) # muestra el valor de la variable pais

notas = [15, 20, 18, 10, 5] # crea una lista de notas

for nota in notas: # recorre la lista de notas y asigna cada elemento a la variable nota
    if nota > 10: # si la nota es mayor o igual a 10
        print("Aprobado") # muestra "Aprobado"
    else: # si la nota es menor a 10
        print("Desaprobado") # muestra "Desaprobado"


cadena = "Hola mundo" # crea una cadena de texto
vocales = ["a", "e", "i", "o", "u"] # crea una lista de vocales


for letra in cadena: # recorre la cadena de texto y asigna cada caracter a la variable letra
    if letra in vocales: # si la letra es una vocal
        print(letra) # muestra la letra

animales = ["perro", "gato", "conejo", "loro"] # crea una lista de animales
for animal in animales: # recorre la lista de animales y asigna cada elemento a la variable animal
    if animal == "gato": # si el animal es un gato
        print("El gato es un felino") # muestra "El gato es un felino"
        break # rompe el bucle y sale del mismo
    
    if animal == "loro": # si el animal es un loro
        print("El loro es un ave") # muestra "El loro es un ave"
        continue # salta a la siguiente iteracion del bucle 
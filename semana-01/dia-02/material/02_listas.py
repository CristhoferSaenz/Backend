# listas - arrays

notas_alunos = [15, 20, 18, 10, 5]
lista_de_lista = [[1,2], ["calcetin", 4]]

print(notas_alunos[-1]) # mustra el ultimo elemento de la lista

print(lista_de_lista[0][1]) #  muestra el primer elemento de la lista y el segundo elemento de la sublista

frutas = ["manzana", "pera", "platano", "naranja"]

frutas[3] = "kiwi" # cambia el valor del elemento en la posicion 3

frutas + ["sandia", "melon"] # concatena dos listas

mas_frutas = frutas + ["sandia", "melon"] # crea una nueva lista con la concatenacion de las dos listas

print(mas_frutas) # muestra la nueva lista
print(frutas) # muestra la lista original


len(frutas) # devuelve la cantidad de elementos de la lista

paises = ["Argentina", "Brasil", "Chile", "Uruguay","Brasil"] # crea una lista de paises

paises.append("Paraguay") # agrega un elemento al final de la lista
paises.count("Brasil") # devuelve la cantidad de veces que se repite un elemento en la lista


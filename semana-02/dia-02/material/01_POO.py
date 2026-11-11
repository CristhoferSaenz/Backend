 # POO: Programacion Orientada a Objetos 
# ES un paradigma de programacion, vamos a organizar nuestro codigo
# mediante clases y objetos
# Es representar a los elementos del mundo real, dentro de un programa

#Mundial 2026

nombre1 = "Messi"
edad1 = 37
posicion1 = "Delantero"
equipo1 = "Argentina"

nombre2 = "Mbappe"
edad2 = 27
posicion2 = "Delantero"
equipo2 = "Francia"

# Para solucinar el problema de arriba, usaremos las clases.
# Que es una clase? (Plano)
# Define las caracteristicas

class Jugador:
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre= nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
    def correr(self):
        print(f"El jugador {self.nombre} esta corriendo")
    def mostrar_info(self):
        print(f"{self.nombre} - {self.edad} años - {self.posicion}")
    def anotar_gol(self,equipo_rival):
        print(f"El jugador {self.nombre} anoto un gol contra {equipo_rival}") 

messi = Jugador("Lionel Messi", 37, "Delantero","Argentina")
mbappe = Jugador("Kylian Mbappe", 27, "Delantero","Francia")

messi.correr()
messi.mostrar_info()
mbappe.anotar_gol("Argentina")


#Pilares del POO
#astraccion
#polimorfismo
#herencia
#encapsulameinto

#abstracion
#Significa extrare las propiedades y metodos 
class Equipo:
    def __init__ (self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"Jugador insertado exitosamente")

brasil = Equipo("Seleccion de Brasil", "Brasil")

ronaldo = Jugador("Ronaldo", 29, "Delantero", "Seleccion de Brasi")
rivaldo = Jugador("Rivaldo", 28, "Delantero", "Seleccion de Brasil")
Ronaldinho = Jugador("Ronaldinho", 27, "Mediocampista", "Seleccion de Brasil")

brasil.agregar_jugador(ronaldo)

print(brasil.jugadores)

# Polimorfismo
# Significad que una clse puede tomar muchas formas

Cristiano_ronaldo = Jugador("Cristiano Ronaldo", 41, "volante", "Seleccion de Portugues")

#herencia
#vas a heredar el comportamiento de la porpiedades y los metodos a la clase hija 


class JugadorPadre:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
        pass
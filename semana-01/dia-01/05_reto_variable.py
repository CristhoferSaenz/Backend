
nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
ciudad=input("Ingrese su ciudad: ")
lenguaje=input("Ingrese su lenguaje de programación favorito: ")

print("Hola, mi nombre es", nombre, ", tengo", edad, "años, vivo en", ciudad, "y mi lenguaje de programación favorito es", lenguaje)

print(nombre,type(nombre))
print(edad,type(edad))  

anio_nacimiento=2026-int(edad)
print("Nací en el año", anio_nacimiento)    

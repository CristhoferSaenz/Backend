
nombre = input("Ingrese su nombre: ")
tiene_dni = input("¿Tiene DNI? (s/n): ")
edad = int(input("Ingrese su edad: "))

if not tiene_dni == "S":
    print("No puede votar")
elif edad < 16:
    print("No puedes votar, eres menor de edad")
elif edad <= 17:
    print("Voto optativo")
elif edad <= 69:
    print("Voto obligatorio")
else:
    print("Voto optativo, por tu edad mayor de 70")
    
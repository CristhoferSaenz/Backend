password = ""
valido = False

while not valido:
    password = input("Ingrese su contraseña: ")
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    elif not any(char.isdigit() for char in password):
        print("La contraseña debe contener al menos un número.")
    elif not any(char.isupper() for char in password):
        print("La contraseña debe contener al menos una letra mayúscula.")
    else:
        valido = True
print("Contraseña válida.")

def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
        return numero
    except Exception:
        print("Error: Debe ingresar un número entero.")

edad = pedir_entero("Ingrese su edad: ")
print(f"Su edad es: {edad}")    
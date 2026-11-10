def saludar (nombre,apellido):
    print(f"Hola, {nombre} {apellido}, ¿cómo estás?")
    print("Bienvenido a la función de saludo.")

saludar("Juan", "Pérez")

def sumar(a, b):
    total = a + b
    return total

## *args: permite recibir un número variable de argumentos posicionales
def mostar_argumentos(*args):
    total = 0
    for arg in args:
        total += arg    
    print(f"La suma de los argumentos es: {total}")
    return total

mostar_argumentos(1, 2, 3, 4, 5)

## **kwargs: permite recibir un número variable de argumentos con nombre
def calcular_area(**kwargs):
    if "base" in kwargs and "altura" in kwargs:
        area = kwargs["base"] * kwargs["altura"] / 2
        print(f"El área del triángulo es: {area}")
        return area
    else:
        print("Faltan argumentos para calcular el área.")
        return None 
print(calcular_area(base=5, altura=10))

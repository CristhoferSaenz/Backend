#crear fucion pedir_notas(mensaje) que pida un entero y verifique que sea un entero entre 0 y 20, si no es un entero o no esta en el rango, debe mostrar un mensaje de error y volver a pedir el valor.

def pedir_nota(mensaje):
    try:
        nota = int(input(mensaje))
    except ValueError:
        print("El dato ingresado no es un numero")
        return
    if nota > 20 or nota < 0: 
        print("La nota no puede ser mayor a 20 ni menor a 0")
    return nota

nota1 = pedir_nota("introduce la nota:")
print(nota1)
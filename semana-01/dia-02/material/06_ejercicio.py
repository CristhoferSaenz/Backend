
clientes = [
    {"nombre": "Ana", "deuda": 150.00, "dias_atraso": 45},
    {"nombre": "Luis", "deuda": 0, "dias_atraso": 0},
    {"nombre": "Sofia", "deuda": 320.50, "dias_atraso": 60},
    {"nombre": "Carlos", "deuda": 75, "dias_atraso": 15},
    {"nombre": "Marta", "deuda": 0, "dias_atraso": 0},
]

mayor_deuda = clientes[0]

for cliente in clientes:

    if cliente["deuda"] > 0:
        print(f"El cliente {cliente['nombre']} tiene una deuda de {cliente['deuda']} y lleva {cliente['dias_atraso']} dias atrasado.")

    if cliente["deuda"] > 100 and cliente["dias_atraso"] > 30:
        print(f"El cliente {cliente['nombre']} tiene una deuda grave de {cliente['deuda']}.")

    if cliente["deuda"] > mayor_deuda["deuda"]:
        mayor_deuda = cliente

    if cliente["deuda"] == 0:
        print(f"El cliente {cliente['nombre']} no tiene deudas.")

print(f"El cliente con mayor deuda es {mayor_deuda['nombre']} con una deuda de {mayor_deuda['deuda']}.")

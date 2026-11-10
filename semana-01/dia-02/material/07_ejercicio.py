# INTERBANK
# El siguiente usuario esta teniendo los siguientes movimientos
movimientos = [
    { "fecha": "2024-01-15", "tipo": "deposito", "monto": 1500.00},
    { "fecha": "2024-01-20", "tipo": "retiro", "monto": 200.00},
    { "fecha": "2024-02-05", "tipo": "deposito", "monto": 500.00},
    { "fecha": "2024-02-10", "tipo": "retiro", "monto": 100.00},
    { "fecha": "2024-02-15", "tipo": "deposito", "monto": 300.00},
    { "fecha": "2024-02-20", "tipo": "retiro", "monto": 50.00},
    { "fecha": "2024-02-25", "tipo": "deposito", "monto": 1000.00 }
]

total_depositos = 0
total_retiros = 0


# 01. Sumar todos los depositos
for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        total_depositos += movimiento["monto"]

print(f"El total de depositos es: {total_depositos}")
# 02. Sumar todos los retiros
for movimiento in movimientos:
    if movimiento["tipo"] == "retiro":
        total_retiros += movimiento["monto"]
print(f"El total de retiros es: {total_retiros}")

# 03. Calcular el balance final (depositos - retiros)

for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        total_depositos += movimiento["monto"]
    elif movimiento["tipo"] == "retiro":
        total_retiros += movimiento["monto"]

print(f"El balance final es: {total_depositos - total_retiros}")

# 04. Mostrar el deposito mas grande
for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        if "mayor_deposito" not in locals() or movimiento["monto"] > mayor_deposito["monto"]:
            mayor_deposito = movimiento
print(f"El deposito mas grande es de {mayor_deposito['monto']} el dia {mayor_deposito['fecha']}.")

# 05. Mostrar el retiro mas grande

for movimiento in movimientos:
    if movimiento["tipo"] == "retiro":
        if "mayor_retiro" not in locals() or movimiento["monto"] > mayor_retiro["monto"]:
            mayor_retiro = movimiento
print(f"El retiro mas grande es de {mayor_retiro['monto']} el dia {mayor_retiro['fecha']}.")

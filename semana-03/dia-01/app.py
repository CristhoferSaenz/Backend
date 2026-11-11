from flask import Flask

app = Flask(__name__)
jugadores = [
    {"id": 1, "nombre": "Paolo Guerrero", "edad": 41, "posicion": "Delantero", "equipo": "Alianza Lima", "seleccion": "Peru"},
    {"id": 2, "nombre": "Andre Carrillo", "edad": 33, "posicion": "Extremo", "equipo": "Al Hilal", "seleccion": "Peru"},
    {"id": 3, "nombre": "Renato Tapia", "edad": 29, "posicion": "Mediocampista", "equipo": "Leganes", "seleccion": "Peru"},
    {"id": 4, "nombre": "Lionel Messi", "edad": 38, "posicion": "Delantero", "equipo": "Inter Miami", "seleccion": "Argentina"},
    {"id": 5, "nombre": "Vinicius Jr", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 6, "nombre": "Luis Diaz", "edad": 28, "posicion": "Extremo", "equipo": "Liverpool", "seleccion": "Colombia"},
    {"id": 7, "nombre": "Federico Valverde", "edad": 27, "posicion": "Mediocampista", "equipo": "Real Madrid", "seleccion": "Uruguay"},
    {"id": 8, "nombre": "Rodrygo", "edad": 25, "posicion": "Extremo", "equipo": "Real Madrid", "seleccion": "Brasil"},
    {"id": 9, "nombre": "Julian Alvarez", "edad": 26, "posicion": "Delantero", "equipo": "Manchester City", "seleccion": "Argentina"},
    {"id": 10, "nombre": "Christian Cueva", "edad": 33, "posicion": "Mediocampista", "equipo": "Cienciano", "seleccion": "Peru"},
]

@app.route("/")
def saludar():
    return "<p> Bienvenidos Comensales <p>" 
@app.route("/milanesa")
def preparar():
    print("Preparando...")
    return {
        "msg": "La milanesa esta prepara",
        "author": "El chef"
    }
@app.route("/jugadores")
def jugadores_mayores():
    jugadores_adultos = []
    for jugador in jugadores:
        if jugador["edad"]>=28:
            jugadores_adultos.append(jugador)
    return{
        "msg":"los jugadores mayores de 28 son",
        "resultados":jugadores_adultos
    }

@app.route("/jugador/<int:id>")
def obtener_jugador(id):
    jugador_econtrado = {}
    for jugador in jugadores:
        if jugador["id"] == id:
            jugador_encontrado = jugador
            break
    return{
        "msg": "jugador encontrado",
        "data": jugador_encontrado
    }




app.run()
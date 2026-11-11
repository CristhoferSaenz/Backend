import random


class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.__creditos = creditos  # Saldo protegido
        self.total_apostado = 0
        self.total_ganado = 0
        self.simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]

    @property
    def creditos(self):
        # Permite consultar el saldo, pero no asignarle uno desde fuera.
        return self.__creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

    def girar(self):
        resultado = [random.choice(self.simbolos) for _ in range(3)]
        print("Resultado:", " | ".join(resultado))
        return resultado

    def _jugar_con_reglas(
        self,
        apuesta,
        multiplicador_tres=10,
        simbolo_especial=None,
        multiplicador_especial=0
    ):
        if apuesta <= 0:
            print("La apuesta debe ser mayor que cero.")
            return

        if apuesta > self.__creditos:
            print(f"No tienes suficientes créditos. Dispones de S/ {self.creditos}.")
            return

        self.__creditos -= apuesta
        self.total_apostado += apuesta

        resultado = self.girar()
        premio = 0

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * multiplicador_tres
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            premio = apuesta * 2

        if simbolo_especial is not None and simbolo_especial in resultado:
            premio_extra = apuesta * multiplicador_especial
            premio += premio_extra
            print(f"Premio extra por {simbolo_especial}: S/ {premio_extra}")

        if premio > 0:
            print(f"Ganaste S/ {premio}")
            self.__creditos += premio
            self.total_ganado += premio
        else:
            print("Lo siento, perdiste.")

        self.mostrar()

    def jugar(self, apuesta):
        self._jugar_con_reglas(apuesta)


class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["🍒", "🍋", "🍊"]


class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["7️⃣", "💎", "🔔"]


class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷"]

    def jugar(self, apuesta):
        # En esta máquina, tres iguales pagan x15.
        # Si aparece Perú, también hay un premio extra de x3.
        self._jugar_con_reglas(
            apuesta,
            multiplicador_tres=15,
            simbolo_especial="🇵🇪",
            multiplicador_especial=3
        )


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Escribe un número entero.")


def jugar_maquina(maquina):
    print(f"\nEntraste a {maquina.nombre}")

    while maquina.creditos > 0:
        maquina.mostrar()
        apuesta = leer_entero("¿Cuánto quieres apostar? (0 para volver): ")

        if apuesta == 0:
            break

        maquina.jugar(apuesta)

    if maquina.creditos == 0:
        print(f"{maquina.nombre} se quedó SIN CRÉDITOS.")


def mostrar_estadisticas(maquinas):
    print("\n--- Estadísticas de las máquinas ---")

    for maquina in maquinas:
        print(f"\n{maquina.nombre}")
        print(f"Créditos actuales: S/ {maquina.creditos}")
        print(f"Total apostado: S/ {maquina.total_apostado}")
        print(f"Total ganado: S/ {maquina.total_ganado}")


def mostrar_resumen(maquinas):
    creditos = sum(maquina.creditos for maquina in maquinas)
    apostado = sum(maquina.total_apostado for maquina in maquinas)
    ganado = sum(maquina.total_ganado for maquina in maquinas)

    print("\n--- Resumen general del casino ---")
    print(f"Créditos que quedan en las máquinas: S/ {creditos}")
    print(f"Total apostado: S/ {apostado}")
    print(f"Total pagado en premios: S/ {ganado}")
    print(f"Balance del casino: S/ {apostado - ganado}")


def main():
    maquinas = [
        TragamonedasFrutas("La Frutal", 200),
        TragamonedasClasico("La Clásica", 300),
        TragamonedasMundial("Mundial 2026", 150)
    ]

    while True:
        print("\n🎰 CASINO ROYALE 🎰")

        for numero, maquina in enumerate(maquinas, start=1):
            if maquina.creditos == 0:
                saldo = "SIN CRÉDITOS"
            else:
                saldo = f"S/ {maquina.creditos}"

            print(f"{numero}. {maquina.nombre} ({saldo})")

        print("4. Mostrar estadísticas de todas")
        print("5. Salir")

        opcion = leer_entero("Elige una opción: ")

        if 1 <= opcion <= 3:
            jugar_maquina(maquinas[opcion - 1])
        elif opcion == 4:
            mostrar_estadisticas(maquinas)
        elif opcion == 5:
            mostrar_resumen(maquinas)
            print("Gracias por jugar.")
            break
        else:
            print("Esa opción no existe.")


if __name__ == "__main__":
    
    main()
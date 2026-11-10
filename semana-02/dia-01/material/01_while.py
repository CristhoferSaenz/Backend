# vidas de juego solo 3, cuando se acaban las vidas el juego termina
vidas = 3
while vidas > 0:
    print(f"Tienes {vidas} vidas restantes.")   
    repuesta = input("¿Quieres perder una vida? (s/n): ")
    if repuesta.lower() == "s":
        vidas -= 1
        print("Has perdido una vida.")  

print("¡Juego terminado! No te quedan vidas.")     
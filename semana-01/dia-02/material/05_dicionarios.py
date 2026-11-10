#Diccionario
##Un diccionario es una estructura de datos que permite almacenar pares de clave-valor.

superheroe = {
    "nombre": "Batman", # clave: valor  
    "edad": 35, # clave: valor
    "poderes": ["inteligencia", "fuerza", "velocidad"], # clave: valor
    "volar": False, # clave: valor
    "amigos": ["Robin", "Alfred", "Comisionado Gordon"] # clave: valor
}   

superheroe["nombre"] # accede al valor de la clave "nombre" 
superheroe.get("nombre") # accede al valor de la clave "nombre" usando el metodo get()

superheroe["ciudad"] = "Gotham" # agrega una nueva clave-valor al diccionario
superheroe["nombre"] = "Bruce Wayne" # modifica el valor de la clave "nombre"
superheroe["edad"] = 36 # modifica el valor de la clave "edad"

superheroe.pop("volar") # elimina la clave-valor "volar" del diccionario

print(superheroe) # muestra el diccionario completo 

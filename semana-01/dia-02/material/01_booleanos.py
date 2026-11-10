# los booleanos son un tipo de dato que solo puede tener dos valores: True o False.
#and es el operador lógico que devuelve True si ambos operandos son True, de lo contrario devuelve False.

print(True and True) # True 
print(True and False) # False


dni= true
mayor_de_edad= true

if dni and mayor_de_edad:
    print("adelante, puedes entrar al bar")
else:
    print("no puedes entrar al bar")    


#or es el operador lógico que devuelve True si al menos uno de los operandos es True    

amigo_promotor= false
pulsera_verde= true

if amigo_promotor or pulsera_verde:
    print("puedes entrar al bar")
else:
    print("no puedes entrar al bar")    
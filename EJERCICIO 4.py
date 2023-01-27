## EJERCICIO 4
## - Escribir una función que determine la frecuencia de cada carácter en una cadena dada y devuelva un diccionario.
def contador(cadena):
    cadena = cadena.split()
    conta = {}
    for i in cadena:
        if i in conta:
            conta[i] += 1
        else:
            conta[i]= 1
    return conta
cadena = "dame , dame que tengo mucha sed"
print(contador(cadena))
## EJERCICIO 2
## - Escribir una función que determine la longitud de la subcadena más larga que no contiene ninguna letra repetida.
def longitud (cadena):
    longitud_cadena=[]
    for n in cadena:
        longitud_cadena.append((len(n),n))
    longitud_cadena.sort()
    return longitud_cadena[-1][1]
cadena=['perro','gato','caracol','rata']
print(longitud(cadena))
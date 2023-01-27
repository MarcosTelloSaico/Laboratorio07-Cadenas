## EJERCICIO 3
## - Escribir una función que divida una cadena dada en una lista de subcadenas cada vez que aparezca un carácter específico.
def dividir_subcadenas(cadena):
    cadena = cadena.split("*",8)
    return cadena
print(dividir_subcadenas("Hola*esto*es*un*texto*que*servirá*de*ejemplo"))
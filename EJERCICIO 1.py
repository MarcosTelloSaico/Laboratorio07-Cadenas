## - Escribir una función que determine si una cadena es un palíndromo (se lee igual en ambos sentidos) o no:
def palindromo(cadena):
    return cadena == cadena[::-1]
print(palindromo("ana"))

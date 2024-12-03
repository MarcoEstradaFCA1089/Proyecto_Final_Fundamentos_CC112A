#Programa en el que verifica si una cadena ingresada es un palíndromo

def Palindromo(texto):# Convertimos todo el texto a minúsculas y eliminamos caracteres no alfabéticos
    
    texto = ''.join(letra for letra in texto.lower() if letra.isalpha())
    
    return texto == texto[::-1]

cadena = input("Ingrese una cadena: ")# Pedimos al usuario que ingrese una cadena

if Palindromo(cadena):# Llamamos a la función Palindromo para verificar si la cadena es un palíndromo
    
    print("Es un palíndromo.")# Si la función devuelve True, significa que es un palíndromo
else:
    
    print("No es un palíndromo.")# Si la función devuelve False, significa que no es un palíndromo


"""
Salida del programa:

Ingrese una cadena: Anita lava la tina
Es un palíndromo.

"""

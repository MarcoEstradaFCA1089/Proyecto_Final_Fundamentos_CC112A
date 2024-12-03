#Programa para poder calcular el factorial de un número con uso de funciones en Python

def factorial(n):# Creamos una función que nos permita hallar el factorial de un número dado por el usuario
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def mostrar_factorial():# Creamos otra función tal que llamarla, el programa solicitará al usuario que ingrese un número.
    try:# Manejamos excepciones como "try y exceptValueError" para asegurarnos de que el usuario ingrese un número válido
        n = int(input("Ingrese un número entero para calcular su factorial: "))
        if n < 0:
            print("El factorial no está definido para números negativos.")
        else:
            fact = factorial(n)
            print(f"El factorial del número {n} es:", end=" ")
            for i in range(1, n + 1):
                if i == n:
                    print(f"{i}", end=" ")
                else:
                    print(f"{i} x", end=" ")
            print(f"= {fact}")
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")# En caso se ingrese un número negativo

mostrar_factorial()# Llamamos a la función "mostrar_factorial" para mostrar el factorial
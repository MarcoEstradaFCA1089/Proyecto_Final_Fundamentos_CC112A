#Programa en el que se pide una lista de numeros enteros digitados por el usuario y que clacule la suma de estos, es
#decir que devuelva el resultado

def calcular_suma():
    # Solicitar el tamaño de la lista
    tamaño = int(input("Introduce el tamaño de la lista: "))
    
    # Crear una lista vacía
    numeros = []
    
    # Solicitar los números al usuario
    for i in range(tamaño):
        num = int(input(f"Introduce el número {i+1}: "))
        numeros.append(num)  # Agregar el número a la lista
    
    # Calcular la suma de los elementos de la lista
    suma = sum(numeros)
    
    # Devolver y mostrar el resultado
    return suma

# Ejemplo de uso:
resultado = calcular_suma()
print(f"La suma de los números es: {resultado}")


"""
Salida del programa:

Introduce el tamaño de la lista: 4
Introduce el número 1: 10
Introduce el número 2: 15
Introduce el número 3: 20
Introduce el número 4: 10
La suma de los números es: 55

"""

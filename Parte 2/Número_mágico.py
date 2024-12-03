#Este es un programa en el que el usuario intenta adivinar un número generado aleatoreamente por el ordenador

import random # Importamos el módulo "random", que se utiliza para generar los números aleatorios.

def juego_adivinar_numero():# Definimos la función de entrada y presentación en pantalla
    print("Bienvenido al juego de adivinar el número!")
    print("El número que tendrás que adivinar se encuentra entre 1 y 100. ¡Vamos tu puedes!")
    print("¡Vamos tu puedes!")

    numero_secreto = random.randint(1, 100)# Inicializamos la semilla con un número que se encuentra entre 1 y 100
    intentos_realizados = 0# Colocamos un contador para ver en cuantos intentos logras adivinar el número

    while True:
        intento = int(input("\nIngresa tu número (entre 1 y 100): "))
        intentos_realizados += 1# Va incrementandose tras cada intento fallido

        if intento < numero_secreto:# Estas pistas nos ayudarán a dar con el número según sea el caso
            print("El número es más alto. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es más bajo. Intenta de nuevo.")
        else:
            print(f"\n¡Felicidades! :) ¡Has adivinado el número {numero_secreto} en {intentos_realizados} intentos!")# Una vez adividado el número
            break# Se cierra

def main():# Función principal para iniciar el juego de adivinar el número
    juego_adivinar_numero()

if __name__ == "__main__":
    main()

"""

Salida del programa:

Bienvenido al juego de adivinar el número!
El número que tendrás que adivinar se encuentra entre 1 y 100. ¡Vamos tu puedes!
¡Vamos tu puedes!

Ingresa tu número (entre 1 y 100): 40
El número es más bajo. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 25
El número es más bajo. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 10
El número es más alto. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 15
El número es más alto. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 21
El número es más bajo. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 20
El número es más bajo. Intenta de nuevo.

Ingresa tu número (entre 1 y 100): 18

¡Felicidades! :) ¡Has adivinado el número 18 en 7 intentos!

"""
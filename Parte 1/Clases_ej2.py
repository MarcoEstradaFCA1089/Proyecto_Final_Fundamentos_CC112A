#Programa donde se crea una clase CuentaBancaria con métodos para depositar y retirar dinero en un menu de opciones.

class CuentaBancaria:#Creamos la clase CuentaBancaria
    def __init__(self, saldo_inicial=1000):#Asumimos una cuenta inicial de 1000 dólares
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):# Se tiene la función depositar con su respectivo parámetro
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):# Se tiene la función retirar cierto monto de lo que ya se tiene guardado en la cuenta 
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad}. Saldo actual: ${self.saldo}")
        elif cantidad > self.saldo:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: Cantidad inválida.")
    
    def mostrar_saldo(self):#Función donde le muestra al usuario el saldo disponible
        print(f"Saldo disponible: ${self.saldo}")

def main():# Función principal del programa
    cuenta = CuentaBancaria()

    while True:# Le mostramos al usuario en pantalla el menu con 4 opciones
        print("\nBienvenido a el cajero automático(ATM)")
        print("1. Ingresar dinero en la cuenta")
        print("2. Retirar dinero de la cuenta")
        print("3. Mostrar dinero disponible")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")# Le damos la opción de que pueda elegir una de las opciones

        if opcion == '1':# Le aparecera un cierto texto según halla elegido la opción
            cantidad = float(input("Ingrese la cantidad a depositar: $"))
            cuenta.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: $"))
            cuenta.retirar(cantidad)
        elif opcion == '3':
            cuenta.mostrar_saldo()
        elif opcion == '4':
            print("Gracias por utilizar el cajero automático.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")#En caso ingrese un valor distinto a 1/2/3/4

if __name__ == "__main__":
    main()


"""
Salida del programa:

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 3
Saldo disponible: $1000

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 1
Ingrese la cantidad a depositar: $156
Se han depositado $156.0. Saldo actual: $1156.0

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 2
Ingrese la cantidad a retirar: $80
Se han retirado $80.0. Saldo actual: $1076.0

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 1
Ingrese la cantidad a depositar: $5666
Se han depositado $5666.0. Saldo actual: $6742.0

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 3
Saldo disponible: $6742.0

Bienvenido a el cajero automático(ATM)
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
Seleccione una opción (1/2/3/4): 4
Gracias por utilizar el cajero automático.

"""
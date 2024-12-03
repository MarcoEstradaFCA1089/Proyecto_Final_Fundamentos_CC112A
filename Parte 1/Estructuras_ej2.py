#Implementar un programa que permita representar la información de un estudiante: su nombre, edad y promedio.
# Además, implemente una función función para mostrar los detalles del estudiante.

class Estudiante:
    def __init__(self, nombre, edad, promedio):
        
        self.nombre = nombre  # Inicializamos los atributos de la clase
        self.edad = edad
        self.promedio = promedio
    
    def mostrar_detalles(self):# Función para mostrar los detalles del estudiante
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.promedio}")


def main(): #Función principal
    # Solicitamos los datos del estudiante
    nombre = input("Introduce el nombre del estudiante: ")
    edad = int(input("Introduce la edad del estudiante: "))
    promedio = float(input("Introduce el promedio del estudiante: "))
    
    estudiante = Estudiante(nombre, edad, promedio)# Crear un objeto de la clase Estudiante
    
    # Mostrar los detalles del estudiante
    estudiante.mostrar_detalles()

main()# Llamar a la función principal


"""
Salida del programa:

Introduce el nombre del estudiante: Alex
Introduce la edad del estudiante: 18
Introduce el promedio del estudiante: 14.5
Nombre: Alex
Edad: 18
Promedio: 14.5

"""

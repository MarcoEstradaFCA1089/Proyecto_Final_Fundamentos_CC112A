#Implemente un programa usando funciones para escribir datos en un archivo de texto

def escribir_en_archivo(nombre_archivo, datos):
    # Abrir el archivo en modo escritura ('w')
    with open(nombre_archivo, 'w') as archivo:
        # Escribir los datos en el archivo
        archivo.write(datos)
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Función principal
def main():
    # Solicitar los datos al usuario
    nombre_archivo = input("Introduce el nombre del archivo: ")
    datos = input("Introduce los datos que quieres escribir en el archivo: ")
    
    # Llamar a la función para escribir los datos en el archivo
    escribir_en_archivo(nombre_archivo, datos)
    
    print(f"Datos escritos en el archivo '{nombre_archivo}' con éxito.")

# Llamar a la función principal
main()


"""
Salida del programa:

Introduce el nombre del archivo: datos.txt
Introduce los datos que quieres escribir en el archivo: Este es un archivo de prueba

Datos escritos en el archivo 'datos.txt' con éxito.

"""

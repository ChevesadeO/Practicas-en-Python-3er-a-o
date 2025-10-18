# Importa el módulo subprocess para ejecutar otros scripts
import subprocess
import sys

def mostrar_menu():
    #Muestra el menú de opciones al usuario.
    print("\n--- Menú de Scripts ---")
    print("1. Ejecutar 'Grupo_de_Chevesade.py'")
    print("2. Ejecutar 'Grupo_de_Leonel.py'")
    print("3. Ejecutar 'Grupo_de_srael.py'")
    print("0. Salir")
    print("-----------------------")

def ejecutar_script(nombre_script):
    #Ejecuta un script de Python utilizando subprocess.
    try:
        print(f"\nEjecutando {nombre_script}...")
        
        # Llama a `sys.executable` para usar el mismo intérprete de Python
        subprocess.run([sys.executable, nombre_script], check=True)
        print(f"\n{nombre_script} ha finalizado.")
    except FileNotFoundError:
        print(f"\nError: El archivo {nombre_script} no se encontró.")
    except subprocess.CalledProcessError as e:
        print(f"\nError al ejecutar {nombre_script}: {e}")

def main():
    #Función principal del programa.
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (0-3): ")

        if opcion == '1':
            ejecutar_script('script1.py')
        elif opcion == '2':
            ejecutar_script('script2.py')
        elif opcion == '3':
            ejecutar_script('script3.py')
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 0 y 3.")


    main()
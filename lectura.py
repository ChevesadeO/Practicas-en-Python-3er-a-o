# 1. Abre el archivo en modo lectura ('r' por default, pero es bueno ser explícito)
try:
    with open('datos.txt', 'r', encoding='utf-8') as archivo:
        print("Contenido del archivo:")
        print("--------------------")

        # 2. Itera sobre cada línea del archivo
        for linea in archivo:
            # 3. Muestra la línea. Usamos .strip() para quitar el salto de línea (\n)
            #    al final de cada línea, para una salida más limpia.
            linea_limpia = linea.strip()
            print(f"Leído: {linea_limpia}")

# Manejo de error si el archivo no existe
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no se encontró.")

# Manejo de otros posibles errores de E/S
except IOError:
    print("Error: No se pudo leer el archivo.")
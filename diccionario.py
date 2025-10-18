#Diccionario de simbolos de monedas, con su respectivo correspondencia 
#con al menos 4 monedas y hacer conversion de divisas.

import  stringlite 


# Diccionario de símbolos de monedas
monedas = {
    'USD': '$',     # Dólar estadounidense
    'EUR': '€',     # Euro
    'JPY': '¥',     # Yen japonés
    'KRW': '₩'      # Won surcoreano
}

# Tasas de cambio ficticias respecto al USD
tasas_cambio = {
    'USD': 1.0,
    'EUR': 0.94,
    'JPY': 149.5,
    'KRW': 1300.0
}

# Lista de monedas disponibles
lista_monedas = list(monedas.keys())

def mostrar_monedas():
    print("\nMonedas disponibles:")
    for i, moneda in enumerate(lista_monedas):
        print(f"{i + 1}. {moneda} ({monedas[moneda]})")

def seleccionar_moneda(mensaje):
    while True:
        try:
            mostrar_monedas()
            opcion = int(input(mensaje))
            if 1 <= opcion <= len(lista_monedas):
                return lista_monedas[opcion - 1]
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def convertir_divisa(cantidad, moneda_origen, moneda_destino):
    # Paso 1: Convertir la cantidad a la base (USD)
    cantidad_en_usd = cantidad / tasas_cambio[moneda_origen]
    # Paso 2: Convertir de la base (USD) a la moneda de destino
    cantidad_convertida = cantidad_en_usd * tasas_cambio[moneda_destino]
    simbolo = monedas[moneda_destino]
    # Formatear el resultado a 2 decimales y añadir el símbolo
    return f"{simbolo}{cantidad_convertida:.2f}"

# Programa principal
print(" Bienvenido al convertidor de divisas ")

#Selección de Monedas
moneda_origen = seleccionar_moneda("Selecciona la moneda de origen (número): ")
moneda_destino = seleccionar_moneda_moneda("Selecciona la moneda de destino (número): ")

#Entrada de Cantidad con Validación 
while True:
    try:
        cantidad_input = input(f"Ingrese la cantidad en {moneda_origen}: ")
        cantidad = float(cantidad_input)
        
        #Validación de Mejora: La cantidad debe ser positiva
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número positivo para la conversión.")
            
    except ValueError:
        print("Por favor, ingresa una cantidad válida (un número).")

#Resultado de la Conversión 
resultado = convertir_divisa(cantidad, moneda_origen, moneda_destino)
print(f"\n {cantidad:.2f} {moneda_origen} equivale a {resultado} {moneda_destino}")



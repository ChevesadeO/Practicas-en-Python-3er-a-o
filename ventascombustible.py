# Precios por litro
precios = {
    1: 0.92,  # Diesel
    2: 0.88,  # Gasolina 91
    3: 0.92   # Gasolina 95
}

# Acumuladores
totales = {
    1: {"litros": 0, "galones": 0, "dinero": 0, "conteo": 0, "M": 0, "T": 0},
    2: {"litros": 0, "galones": 0, "dinero": 0, "conteo": 0, "M": 0, "T": 0},
    3: {"litros": 0, "galones": 0, "dinero": 0, "conteo": 0, "M": 0, "T": 0}
}

# Conversión
LITRO_A_GALON = 0.2642

print(" Registro de ventas gasolinera ")
while True:
    servicio = int(input("Ingrese tipo de servicio (1: Diesel, 2: Gas91, 3: Gas95, 0: salir): "))
    if servicio == 0:
        break
    
    if servicio not in precios:
        print("Servicio inválido.")
        continue
    
    jornada = input("Jornada (M/T): ").upper()
    if jornada not in ["M", "T"]:
        print("Jornada inválida.")
        continue
    
    litros = float(input("Litros vendidos: "))
    
    # Calcular venta
    dinero = litros * precios[servicio]
    galones = litros * LITRO_A_GALON
    
    # Acumular
    totales[servicio]["litros"] += litros
    totales[servicio]["galones"] += galones
    totales[servicio]["dinero"] += dinero
    totales[servicio]["conteo"] += 1
    totales[servicio][jornada] += dinero

#Reporte final 
print("\n=== Reporte del día ===")
for s in totales:
    print(f"\nServicio {s}:")
    print(f"  Litros vendidos: {totales[s]['litros']:.2f}")
    print(f"  Galones vendidos: {totales[s]['galones']:.2f}")
    print(f"  Total dinero: ${totales[s]['dinero']:.2f}")
    print(f"  Número de servicios: {totales[s]['conteo']}")

# Servicio con más ventas en dinero
mayor_servicio = max(totales, key=lambda x: totales[x]["dinero"])
print(f"\nEl servicio con más ventas en dinero fue el {mayor_servicio} con ${totales[mayor_servicio]['dinero']:.2f}")

# Jornada donde se vendió más en ese servicio
jornada_mayor = "mañana" if totales[mayor_servicio]["M"] > totales[mayor_servicio]["T"] else "tarde"
print(f"Y se vendió más en la {jornada_mayor}.")

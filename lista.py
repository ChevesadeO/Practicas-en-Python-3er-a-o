#ejemplo de una lista en Python en un bucle for desde -1 hasta el final


mi_lista = [1, 2, 3, "cuatro", 5.6]
mi_lista.append(7)
mi_lista.extend([8, "A", 9])
mi_lista.insert(10, "x")
mi_lista.pop(["i"])
for recorrido in mi_lista:
    print(recorrido)

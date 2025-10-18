import streamlit


calculadora = True 
while calculadora: 
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raiz cuadrada")
    print("6. Potencia")
    print("7. Porcentaje")
    print("8. Factorial")
    print("9. Residuo")
    print("10. Salir")

    opcion = input("Seleccione una opción (1-10): ")
    if opcion in ['1', '2', '3', '4', '5', '6', '7', '8']:
        num1 = float(input("Ingrese el primer número: "))
        if opcion in ['1', '2', '3', '4', '6', '7']:
            num2 = float(input("Ingrese el segundo número: "))  
        if opcion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':         
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif opcion == '5':
            if num1 >= 0:
                resultado = num1 ** 0.5
                print(f"El resultado de la raíz cuadrada es: {resultado}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        elif opcion == '6':     
            resultado = num1 ** num2
            print(f"El resultado de la potencia es: {resultado}")
        elif opcion == '7':
            resultado = (num1 * num2) / 100
            print(f"El resultado del porcentaje es: {resultado}")
        elif opcion == '8':
            if num1 >= 0 and num1.is_integer():
                factorial = 1
                for i in range(1, int(num1) + 1):
                    factorial *= i
                print(f"El factorial de {int(num1)} es: {factorial}")
            else:
                print("Error: El factorial solo está definido para números enteros no negativos.")
            if opcion == '9':
                a = int(input("Ingrese el primer numero: "))
                b = int(input("Ingrese el segundo numero:"))  
                residuo = a % b
                print("El resuduao de",a, "entre",b, "es: ")  
    elif opcion == '10':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")
    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        calculadora = False
        print("Gracias por usar la calculadora. ¡Hasta luego!")
#si el usuario no desea continuar se le agradece por usar la calculadora y se termina el programa
    else:
        print("Continuando con la calculadora...") 


 

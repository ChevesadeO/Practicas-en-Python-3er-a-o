def validar_contrasena():
    
    contrasena_correcta = "12345"  # La contraseña que se debe adivinar
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        contrasena_ingresada = input("Ingresa la contraseña: ")

        if contrasena_ingresada == contrasena_correcta:
            print("¡Contraseña correcta! Acceso concedido.")
            return True  # Termina la función al acertar
        else:
            intentos += 1
            print(f"Contraseña incorrecta. Te quedan {max_intentos - intentos} intentos.")

    # Si el bucle termina, significa que se agotaron los intentos
    print("Has agotado tus intentos. Tu cuenta ha sido bloqueada.")
    return False

# Ejecutar la función
validar_contrasena()
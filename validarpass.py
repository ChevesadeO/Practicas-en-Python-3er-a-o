# Dado una contrase;a, validar permitir 3 intentos si falla bloquear, longitud minima de la contrase;a sea de 10 caracteres 

def validar_contrasena():
   
    contrasena_correcta = "123456789ABC"  
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        contrasena_ingresada = input("Por favor, ingrese la contraseña: ")

      
        if len(contrasena_ingresada) < 10:
            print("Error: La contraseña debe tener al menos 10 caracteres.")
            intentos += 1
            print(f"Le quedan {max_intentos - intentos} intentos.")
            continue  

        
        if contrasena_ingresada == contrasena_correcta:
            print("¡Acceso concedido! ")
            return  
        else:
            print("Contraseña incorrecta. Inténtelo de nuevo.")
            intentos += 1
            print(f"Le quedan {max_intentos - intentos} intentos.")

    
    print("Ha superado el número de intentos. El acceso ha sido bloqueado.")

validar_contrasena()


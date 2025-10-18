# Dado una contrase;a, validar permitir 3 intentos si falla bloquear, 
# longitud minima de la contrase;a sea de 10 caracteres 

contrasena = "123456789ABC"
longitud_minima = 10
if len(contrasena) < longitud_minima:
    print(f"La contrase;a debe tener al menos {longitud_minima} caracteres.")
    exit()
intentos = 0

max_intentos = 3

while intentos < max_intentos:
    contrasena_ingresada = input("Ingresa la contraseña: ")
    if contrasena_ingresada == contrasena:
        print("¡Contraseña correcta!")
        break
    else:
        intentos += 1
        print(f"La contraseña no tiene la longitud correcta. Te quedan {max_intentos - intentos} intentos.")

if intentos == max_intentos:
    print("Has agotado tus intentos. Tu cuenta ha sido bloqueada.")
    exit() 
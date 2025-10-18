#basado en el saldo de un cliente asignado a una variable y una clave asignada a a otra variable, simule estas operaciones basicas
#de un cajero, mediante un menu. 
#el usuario no podra ver las opciones del menu hasta que la clave sea correcta y solo tendra 2 intentos para ingresar la clave correcta.
##1. Consultar saldo y regresar al menu
##2. Retirar efectivo 
##sino puede retirar mas dinero del que tiene en el saldo enviar el mensaje de fondos insuficientes y volver al menu
##si puede retirar indicar cual es nuevo saldo  
##3. salir 


#Variables iniciales
saldo = 1000
clave = "0718"
intentos = 0

#Proceso de ingreso de clave
while intentos < 2:
    clave_ingresada = input("Ingrese la clave para acceder al menu: ")
    if clave_ingresada == clave:
        print("Clave correcta. Accediendo al menu...")
        break
    else:
        print("Clave incorrecta. Intente de nuevo.") #Incremento de intentos
        intentos += 1
#Verificacion de intentos 
if intentos == 2:
    print("Demasiados intentos. Saliendo...")
else:
    while True:
        print("Menu:")
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar efectivo")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("Su saldo es:", saldo)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad <= saldo:
                saldo -= cantidad
                print("Retiro exitoso. Su nuevo saldo es:", saldo)
            else:
                print("Saldo insuficiente.")
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            saldo += cantidad
            print("Deposito exitoso. Su nuevo saldo es:", saldo)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
        #1. Consultar saldo y regresar al menu
        #2. Retirar efectivo 
        #sino puede retirar mas dinero del que tiene en el saldo enviar el mensaje de fondos insuficientes y volver al menu
        #si puede retirar indicar cual es nuevo saldo  
        #3. salir 
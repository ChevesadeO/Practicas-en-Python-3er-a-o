#basado en el saldo de un cliente asignado a una variable y una clave asignada a a otra variable, simule estas operaciones basicas
#de un cajero, mediante un menu. 
#el usuario no podra ver las opciones del menu hasta que la clave sea correcta y solo tendra 2 intentos para ingresar la clave correcta.
##1. Consultar saldo y regresar al menu
##2. Retirar efectivo no mayor a 500 y que al enviar el mensaje de exito regrese salga del menu y vuelva a pedir la clave
##sino puede retirar mas dinero del que tiene en el saldo enviar el mensaje de fondos insuficientes y volver al menu
##si puede retirar indicar cual es nuevo saldo  y salir del menu y volver a pedir la clave 
##3. salir 

import tkinter as tk
from tkinter import messagebox  

# Variables globales
saldo = 10000.0
clave = "0718"
intentos = 0
max_intentos = 2    

# Verificar clave
def verificar_clave():
    global intentos
    clave_ingresada = entry_clave.get()
    if clave_ingresada == clave:
        messagebox.showinfo("Acceso", "Clave correcta. Accediendo al menú...")
        mostrar_menu()
    else:
        intentos += 1
        if intentos >= max_intentos:
            messagebox.showerror("Acceso denegado", "Ha excedido el número de intentos.")
            root.destroy()
        else:
            messagebox.showwarning("Clave incorrecta", f"Intento {intentos} de {max_intentos}")
            entry_clave.delete(0, tk.END)

def mostrar_menu():
    frame_login.pack_forget()
    frame_menu.pack(pady=20)

def consultar_saldo():
    messagebox.showinfo("Saldo", f"Su saldo actual es: ${saldo:.2f}")

def retirar_efectivo():
    def procesar_retiro():
        global saldo
        try:
            monto = float(entry_monto.get())
            if monto > saldo:
                messagebox.showerror("Error", "Fondos insuficientes.")
            elif monto > 500:
                messagebox.showerror("Error", "El monto máximo para retirar es $500.")
            else:
                saldo -= monto
                messagebox.showinfo("Éxito", f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
                ventana_retiro.destroy()
                frame_menu.pack_forget()
                frame_login.pack(pady=20)
                entry_clave.delete(0, tk.END)  # <<< limpiar casilla al regresar
            ventana_retiro.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido.")

    ventana_retiro = tk.Toplevel(root)
    ventana_retiro.title("Retiro de efectivo")
    tk.Label(ventana_retiro, text="Monto a retirar:").pack(pady=5)
    entry_monto = tk.Entry(ventana_retiro)
    entry_monto.pack(pady=5)
    tk.Button(ventana_retiro, text="Retirar", command=procesar_retiro).pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cajero Automático")

# Frame de login
frame_login = tk.Frame(root)
tk.Label(frame_login, text="Ingrese su clave:").pack(pady=5)
entry_clave = tk.Entry(frame_login, show="*")
entry_clave.pack(pady=5)
tk.Button(frame_login, text="Ingresar", command=verificar_clave).pack(pady=10)
frame_login.pack(pady=20)

# Frame del menú
frame_menu = tk.Frame(root)
tk.Button(frame_menu, text="1. Consultar saldo", command=consultar_saldo).pack(pady=5)
tk.Button(frame_menu, text="2. Retirar efectivo", command=retirar_efectivo).pack(pady=5)
tk.Button(frame_menu, text="3. Salir", command=root.destroy).pack(pady=5)

# Iniciar la aplicación
root.mainloop()


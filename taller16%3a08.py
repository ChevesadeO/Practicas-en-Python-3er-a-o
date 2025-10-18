#basado en el saldo de un cliente asignado a una variable y una clave asignada a a otra variable, simule estas operaciones basicas
#de un cajero, mediante un menu. 
#el usuario no podra ver las opciones del menu hasta que la clave sea correcta y solo tendra 2 intentos para ingresar la clave correcta.
##1. Consultar saldo y regresar al menu
##2. Retirar efectivo 
##sino puede retirar mas dinero del que tiene en el saldo enviar el mensaje de fondos insuficientes y volver al menu
##si puede retirar indicar cual es nuevo saldo  
##3. salir 

import tkinter as tk
from tkinter import messagebox

# Variables globales
saldo = 1000.0
clave = "0718"
intentos = 0
max_intentos = 2

# Funciones
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
            else:
                saldo -= monto
                messagebox.showinfo("Éxito", f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            ventana_retiro.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido.")

    ventana_retiro = tk.Toplevel(root)
    ventana_retiro.title("Retiro de efectivo")
    tk.Label(ventana_retiro, text="Monto a retirar:").pack(pady=5)
    entry_monto = tk.Entry(ventana_retiro)
    entry_monto.pack(pady=5)
    tk.Button(ventana_retiro, text="Retirar", command=procesar_retiro).pack(pady=10)

def salir():
    messagebox.showinfo("Salir", "Gracias por usar el cajero. Hasta luego!")
    root.destroy()

# Ventana principal
root = tk.Tk()
root.title("Cajero Automático")
root.geometry("300x200")

# Frame de login
frame_login = tk.Frame(root)
frame_login.pack(pady=40)

tk.Label(frame_login, text="Ingrese su clave:").pack(pady=5)
entry_clave = tk.Entry(frame_login, show="*")
entry_clave.pack(pady=5)
tk.Button(frame_login, text="Acceder", command=verificar_clave).pack(pady=10)

# Frame del menú
frame_menu = tk.Frame(root)

tk.Label(frame_menu, text="Menú Principal").pack(pady=5)
tk.Button(frame_menu, text="1. Consultar saldo", command=consultar_saldo).pack(pady=5, fill="x")
tk.Button(frame_menu, text="2. Retirar efectivo", command=retirar_efectivo).pack(pady=5, fill="x")
tk.Button(frame_menu, text="3. Salir", command=salir).pack(pady=5, fill="x")

root.mainloop()
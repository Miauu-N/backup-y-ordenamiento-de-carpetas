import threading
import tkinter as tk
from tkinter import filedialog, simpledialog
from pathlib import Path
import shutil
from ordenar_carpeta import ordenar
from schedule_backup import registrar_backup

def organizar_carpeta():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta a organizar")
    if not carpeta:
        return
    ordenar(carpeta)

def backup():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta a backupear")
    bp = filedialog.askdirectory(title="Seleccionar carpeta donde su creara el backup")
    limite = simpledialog.askinteger(prompt="introduzca la cantidad de copias que desee guardar",title="Limite")
    if not carpeta or not bp or not limite or not limite.is_integer():
        return
    threading.Thread(target=registrar_backup, args=(carpeta, bp, limite), daemon=True).start()


def main():
    root = tk.Tk()
    root.title("Organizador de Archivos")
    root.geometry("400x200")

    # Etiqueta y botón
    btn2 = tk.Button(root, text="Seleccionar carpeta y crear backup", command=backup, font=("Arial", 10))
    btn2.pack(pady=10)

    btn = tk.Button(root, text="Seleccionar carpeta y organizar", command=organizar_carpeta, font=("Arial", 10))
    btn.pack(pady=10)

    root.mainloop()

main()
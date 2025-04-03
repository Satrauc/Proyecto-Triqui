
from tkinter import messagebox

def mostrar_mensaje(winner=None):
    if winner:
        messagebox.showinfo("Fin del juego", f"¡{winner} ha ganado!")
    else:
        messagebox.showinfo("Fin del juego", "¡Empate!")

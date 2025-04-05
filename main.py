import tkinter as tk
from Disenotablero import interfaz_grafica
from LogicaTriqui import  reset_board


# Configuración de la ventana
root = tk.Tk()
root.title("Triqui")
turn = ["X"]

buttons = []


frame = tk.Frame(root)
frame.pack()

triqui.create_board(frame)

interfaz_grafica(root, frame, buttons, turn)



root.mainloop()


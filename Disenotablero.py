import tkinter as tk
from imagen_Botones import on_click
from LogicaTriqui import check_winner, reset_board
from PantallaFin import mostrar_mensaje

def interfaz_grafica(root, frame, buttons, turn):
    for i in range(9):
        button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda i=i: on_click(i, buttons,turn))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

    
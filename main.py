import tkinter as tk
from BotonImagen import on_click
from LogicaTriqui import check_winner, reset_board
from PantallaFin import mostrar_mensaje

root = tk.Tk()
root.title("Triqui")

turn = "X"
buttons = []

winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6)           
]

for i in range(3):
    for j in range(3):
        boton = tk.Button(
            root,
            text="",
            width=10,
            height=4,
            font=("Arial", 20),
            command=lambda b=len(buttons): handle_click(b)
        )
        boton.grid(row=i, column=j)
        buttons.append(boton)


def handle_click(index):
    global turn
    boton = buttons[index]
    if boton['text'] == "":
        boton['text'] = turn
        if not check_winner(winning_combinations, buttons):
            turn = "O" if turn == "X" else "X"


reset_button = tk.Button(root, text="Reiniciar", font=("Arial", 14),
                         command=lambda: reset_board(buttons))
reset_button.pack(pady=10)

root.mainloop()

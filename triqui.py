# triqui.py
import tkinter as tk
from tkinter import messagebox

turn = "X"
buttons = []
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

def check_winner():
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            messagebox.showinfo("Fin del juego", f"¡{buttons[line[0]]['text']} ha ganado!")
            reset_board()
            return True
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Fin del juego", "¡Empate!")
        reset_board()
        return True
    return False

def on_click(index):
    global turn
    if buttons[index]['text'] == "":
        buttons[index]['text'] = turn
        if not check_winner():
            turn = "O" if turn == "X" else "X"

def reset_board():
    global turn
    for button in buttons:
        button['text'] = ""
    turn = "X"

def create_board(frame):
    for i in range(9):
        button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda i=i: on_click(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

def create_reset_button(root):
    return tk.Button(root, text="Reiniciar", command=reset_board, font=("Arial", 14))


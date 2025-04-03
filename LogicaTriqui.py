from tkinter import messagebox
from PantallaFin import mostrar_mensaje

def check_winner(winning_combinations, buttons):
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            mostrar_mensaje(buttons[line[0]]['text'])
            reset_board()
            return True
    if all(button['text'] != "" for button in buttons):
        mostrar_mensaje()
        reset_board(buttons)
        return True
    return False

def reset_board(buttons):
    global turn
    for button in buttons:
        button['text'] = ""
    turn = "X"
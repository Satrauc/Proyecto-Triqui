from tkinter import messagebox

def check_winner(winning_combinations, buttons):
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            messagebox.showinfo("Fin del juego", f"¡{buttons[line[0]]['text']} ha ganado!")
            reset_board()
            return True
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Fin del juego", "¡Empate!")
        reset_board(buttons)
        return True
    return False

def reset_board(buttons):
    global turn
    for button in buttons:
        button['text'] = ""
    turn = "X"
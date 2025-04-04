from PantallaFin import mostrar_mensaje

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
def check_winner(buttons, turn):
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            mostrar_mensaje(buttons[line[0]]['text'])
            reset_board(buttons, turn)
            return True
    if all(button['text'] != "" for button in buttons):
        mostrar_mensaje()
        reset_board(buttons,turn)
        return True
    return False

def reset_board(buttons, turn):
    #global turn
    for button in buttons:
        button['text'] = ""
    turn[0] = "X"
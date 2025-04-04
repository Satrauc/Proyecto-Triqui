from LogicaTriqui import check_winner



def on_click(index, buttons, turn):
    #global turn[0]
    if buttons[index]['text'] == "":
        buttons[index]['text'] = turn[0]
        if not check_winner(buttons, turn):
            turn[0] = "O" if turn[0] == "X" else "X"





from LogicaTriqui import check_winner
def on_click(boton=None):
    global turn
    if boton == "":
        boton = turn
        if not check_winner():
            turn = "O" if turn == "X" else "X"

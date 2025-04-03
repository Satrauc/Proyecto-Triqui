def on_click(index):
    global turn
    if buttons[index]['text'] == "":
        buttons[index]['text'] = turn
        if not check_winner():
            turn = "O" if turn == "X" else "X"

import tkinter as tk
from BotonImagen import BotonImagen
from Disenotablero import crear_tablero
from LogicaTriqui import check_winner, reset_board

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.turn = "X"
        self.buttons = []
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        
        for i in range(3):
            for j in range(3):
                btn = BotonImagen(self.board_frame, i, j, self.on_click)
                btn.grid(row=i, column=j)
                self.buttons.append(btn)
    
    def on_click(self, index):
        if self.buttons[index]['text'] == "":
            self.buttons[index]['text'] = self.turn
            
            if check_winner(self.winning_combinations, self.buttons):
                return
            
            self.turn = "O" if self.turn == "X" else "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

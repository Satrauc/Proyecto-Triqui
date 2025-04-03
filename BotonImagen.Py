buttons = []

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

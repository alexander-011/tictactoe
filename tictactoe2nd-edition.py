import tkinter as tk




class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("131x160")


        self.buttons = []
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                self.buttons[i].append(tk.Button(self.root, width=5, height=2, command=lambda i=i, j=j: self.play(i, j)))
                self.buttons[i][j].grid(row=i, column=j)


        self.player = "X"
        self.result = tk.StringVar()
        self.result.set("Player " + self.player + "'s turn")


        self.result_label = tk.Label(self.root, textvariable=self.result)
        self.result_label.grid(row=3, column=0, columnspan=3)


        self.root.mainloop()


    def play(self, row, col):
        if self.buttons[row][col]["text"] != "":
            return


        self.buttons[row][col].config(text=self.player)
        self.check_win(self.player)


        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"


        self.result.set("Player " + self.player + "'s turn")


    def check_win(self, player):
        for i in range(3):
            if self.buttons[i][0]["text"] == player and self.buttons[i][1]["text"] == player and self.buttons[i][2]["text"] == player:
                self.result.set("Player " + player + " wins!")
                return
            if self.buttons[0][i]["text"] == player and self.buttons[1][i]["text"] == player and self.buttons[2][i]["text"] == player:
                self.result.set("Player " + player + " wins!")
                return


        if self.buttons[0][0]["text"] == player and self.buttons[1][1]["text"] == player and self.buttons[2][2]["text"] == player:
            self.result.set("Player " + player + " wins!")
            return
        if self.buttons[0][2]["text"] == player and self.buttons[1][1]["text"] == player and self.buttons[2][0]["text"] == player:
            self.result.set("Player " + player + " wins!")
            return




TicTacToe()






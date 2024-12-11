import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kryss og Sirkel vs Bot")
        self.window.geometry("400x400")
        self.player_turn = "X"
        self.bot_turn = "O"
        self.buttons = []
        self.restart_button = None
        self.game_over_flag = False

        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=4, width=8, font=('Arial', 20))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if not self.game_over_flag and self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                self.game_over(f"Vinneren er {self.player_turn}")
            elif self.is_draw():
                self.game_over("Uavgjort")
            else:
                self.bot_move()

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def is_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def game_over(self, message):
        self.game_over_flag = True
        messagebox = tk.Message(self.window, text=f"Spillet er over! {message}", bg="red", fg="white", font=('Arial', 16))
        messagebox.grid(row=3, column=0, columnspan=3, pady=20)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_game, bg="green", fg="white", font=('Arial', 16))
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)

    def restart_game(self):
        for row in self.buttons:
            for button in row:
                button.grid_forget()
        if self.restart_button:
            self.restart_button.grid_forget()

        self.buttons = []
        self.game_over_flag = False
        self.create_board()

    def bot_move(self):
        if not self.game_over_flag:
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j]['text'] = self.bot_turn
                        if self.check_win():
                            self.game_over(f"Vinneren er BOT")
                            return
                        self.buttons[i][j]['text'] = ""

            if random.random() < 0.7:
                for i in range(3):
                    for j in range(3):
                        if self.buttons[i][j]['text'] == "":
                            self.buttons[i][j]['text'] = self.player_turn
                            if self.check_win():
                                self.buttons[i][j]['text'] = self.bot_turn
                                return
                            self.buttons[i][j]['text'] = ""

            if self.buttons[1][1]['text'] == "":
                self.buttons[1][1]['text'] = self.bot_turn
                return

            for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = self.bot_turn
                    return

            for i, j in [(0, 1), (1, 0), (1, 2), (2, 1)]:
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j]['text'] = self.bot_turn
                    return

            if self.is_draw():
                self.game_over("Uavgjort")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

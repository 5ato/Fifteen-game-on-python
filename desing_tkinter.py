from tkinter import Tk, Canvas

from game import GameTag


class GameGUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logic_game = GameTag()
        self.title('Пятнашка Игра')
        self.canvas = Canvas(self, width=self.logic_game.size_board * self.logic_game.pixel_square,
                             height=self.logic_game.size_board * self.logic_game.pixel_square, bg='#71717a')
        self.canvas.pack()
        self.draw_canwas()
        self.canvas.bind('<Button-1>', self.click)

    def draw_canwas(self):
        self.canvas.delete('all')
        for i in range(self.logic_game.size_board):
            for j in range(self.logic_game.size_board):
                index = self.logic_game.game[self.logic_game.size_board * i + j]
                if index != self.logic_game.empty_square:
                    self.canvas.create_rectangle(j * self.logic_game.pixel_square, i * self.logic_game.pixel_square,
                                                 j * self.logic_game.pixel_square + self.logic_game.pixel_square,
                                                 i * self.logic_game.pixel_square + self.logic_game.pixel_square,
                                                 fill='#9d174d', outline='#e0f2fe')
                    self.canvas.create_text(j * self.logic_game.pixel_square + self.logic_game.pixel_square / 2,
                                            i * self.logic_game.pixel_square +  self.logic_game.pixel_square / 2,
                                            text=str(index), fill='#e0f2fe')
                    
    def click(self, event):
        x, y = event.x, event.y

        x, y = x // self.logic_game.pixel_square, y // self.logic_game.pixel_square

        border_index = x + (y * self.logic_game.size_board)
        empty_index = self.get_empty(border_index)
        self.logic_game.game[border_index], self.logic_game.game[empty_index] = self.logic_game.game[empty_index], self.logic_game.game[border_index]

        self.draw_canwas()

        if self.logic_game.game == self.logic_game.correct_game:
            self.quit()

    def get_empty(self, index):
        empty_index = self.logic_game.game.index(self.logic_game.empty_square)
        path_empty = abs(empty_index - index)
        if path_empty == self.logic_game.size_board:
            return empty_index
        elif path_empty == 1:
            max_index = max(index, empty_index)
            if max_index % self.logic_game.size_board != 0:
                return empty_index
        return index
    
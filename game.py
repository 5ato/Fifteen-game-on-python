from random import shuffle, choice


class GameTag:
    __slots__ = ('size_board', 'empty_square', 'game', 'pixel_square', 'correct_game')

    def __init__(self, size: int = 4):
        self.size_board: int = size
        self.empty_square: int = size ** 2
        self.game: list[int] = list(range(1, self.empty_square + 1))
        self.correct_game = self.game.copy()
        shuffle(self.game)
        print(self.game)
        self.pixel_square = 80
            
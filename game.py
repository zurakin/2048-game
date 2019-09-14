import random
import tile
from PIL import ImageTk

class Game:
    def __init__(self,window):
        self.window = window
        self.board = {(i,j): None for i in range(4) for j in range(4)}
        [self.randfill() for i in range(6)]
        self.images = []
        self.trash = []

    def randfill(self):
        pos = random.choice([key for key in self.board.keys() if self.board[key] == None ])
        self.board[pos] = tile.Tile(2,pos)
    def fill(self):
        for i in range(2,4):
            self.board[(0,i)] = tile.Tile(2,(0,i))

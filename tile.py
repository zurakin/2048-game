from PIL import ImageTk ,Image


class Tile():
    def __init__(self,value,pos):
        self.available = True
        self.value = value
        self.update_image()
        self.position = pos
        self.direction = (0, 0)
        self.movements = {
        'up':self.get_up,
        'down':self.get_down,
        'right':self.get_right,
        'left':self.get_left
        }

    def update_image(self):
        path = r'media/{}.png'.format(str(self.value))
        self.image = ImageTk.PhotoImage(file = path)

    def get_up(self):
        return (self.position[0], self.position[1]-1, 0, -1)
    def get_down(self):
        return (self.position[0], self.position[1]+1, 0, 1)
    def get_right(self):
        return (self.position[0]+1, self.position[1], 1, 0)
    def get_left(self):
        return (self.position[0]-1, self.position[1], -1, 0)

    def move(self, game,movement):
        new = self.movements[movement]()[0:2]
        if new[0] not in range(0,4) or new[1] not in range(0,4):
            return False

        if game.board[new] == None:
            game.board[self.position] = None
            self.position = new
            game.board[self.position] = self
            self.direction = (new[2:])
            return True

        if game.board[new].value != self.value:
            return False

        if game.board[new].value == self.value:
            game.board[new].available = False
            game.trash.append(game.board[new])
            self.value = self.value*2
            game.board[self.position] = None
            self.position = new
            game.board[self.position] = self
            self.direction = (new[2:])
            self.update_image()

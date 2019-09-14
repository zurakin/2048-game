from tkinter import *
from PIL import ImageTk


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title('2048 game')
        self.canvas = Canvas(self.window, width = 500, height = 500)
        self.canvas.grid()
        self.bgim = ImageTk.PhotoImage(file = r'media\background.png')
        self.canvas.create_image(0, 0, image = self.bgim, anchor = NW)
        self.window.update()


    def draw(self, game):
        for image in game.images:
            self.canvas.delete(image)

        for pos,tile in game.board.items():
            if tile != None:
                game.images.append(self.canvas.create_image( 20 + 120 * pos[0], 20 + 120*pos[1], image = tile.image, anchor = NW))
                self.window.update()

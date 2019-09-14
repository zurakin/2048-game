import window
import game


def move(direction,keys):
    for i in range(4):
        tiles = [game.board[key] for key in keys if game.board[key] != None ]
        for tile in tiles:
            tile.move(game, direction)
    game.randfill()
    root.draw(game)

def up(*args):
    keys = [(i,j) for j in range(4) for i in range(4)]
    move('up',keys)

def down(*args):
    keys = [(i,j) for j in range(4) for i in (3,2,1,0)]
    move('down',keys)

def right(*args):
    keys = [(i,j) for j in (3,2,1,0) for i in range(4)]
    move('right',keys)

def left(*args):
    keys = [(i,j) for j in range(4) for i in range(4)]
    move('left',keys)

root = window.Window()
root.window.bind('<Up>',up)
root.window.bind('<Down>',down)
root.window.bind('<Right>',right)
root.window.bind('<Left>',left)
game = game.Game(window)
root.draw(game)

root.window.mainloop()

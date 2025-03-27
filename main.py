from model import *
from view import *

if __name__ == '__main__':
    size = 3
    model = Board(size)
    view = BoardView(model)
    view.run()
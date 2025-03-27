import pygame
from model import *

class BoardView:
    def __init__(self, model:Board, screen_size=600):
        self.board:Board = model
        self.scree_size = screen_size
        initial_coord = (50, 50)
        end_coord = (300, 300)
        self.cell_size = int((end_coord[0] - initial_coord[0]) / self.board.size)

        self.view_model = getModelView(self, screen_size) #  Cada i,j en la matrix sera de la forma ((x_0, x_size),(y_0, y_size)) que indicara la extension de la casilla en x y en y respectivamente
        pygame.init()
        self.screen = pygame.display.set_mode((screen_size, screen_size))
        self.colors = {'White': (0,0,0), 'Black': (255,255,255), 'Gray': (100,100,100)}

    def drawBoard(self):
        self.screen.fill(self.colors['White'])
        for row in self.board.board:
            for col in row:
                col_:Tile = col
                col_.image = pygame.transform.scale(col_.image, (self.cell_size-4, self.cell_size-4))
                self.screen.blit(col_.image, (self.view_model[col_.origin_coord[0]][0][0][0], self.view_model[col_.origin_coord[1]][0][0][0]))
        pygame.display.flip()

    def run(self):
        running = True
        self.drawBoard()
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()








def getModelView(board_view:BoardView, scree_size):
    result = []
    
    size = board_view.board.size
    initial_coord = (50, 50)
    end_coord = (300, 300)
    cell_size = int((end_coord[0] - initial_coord[0]) / size)

    for i in range(size):
        row = []
        for j in range(size):             
            initial_x = i*cell_size + initial_coord[0]
            initial_y = j*cell_size + initial_coord[1]
            tile_sizes = ((initial_x, initial_x + cell_size), (initial_y, initial_y + cell_size))
            row.append(tile_sizes)
        result.append(row)
    return result
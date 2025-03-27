import os
import pygame
from itertools import count

import pygame.locals

class Tile:
    def __init__(self, counter, size):
        self.board_size = size
        self.origin_coord = (counter // size, counter % size)
        if self.origin_coord[0] == 0 and self.origin_coord[1] == 0:
            self.isEmptyTile = True
        else:
            self.isEmptyTile = False
        self.coord = (self.origin_coord[0], self.origin_coord[1])
        try:
            image_rute = os.path.join("pictures", f'number{counter+1}.png')
            self.image = pygame.image.load(image_rute)
        except FileNotFoundError:
            print('ruta no encontrada')
    
    def getAdjacentsCoords(self):
        adjacents_coords = []
        if self.coord[0] - 1 >= 0:  # up
            adjacents_coords.append((self.coord[0] - 1, self.coord[1]))
        if self.coord[1] + 1 < self.board_size:  # right
            adjacents_coords.append((self.coord[0], self.coord[1] + 1))
        if self.coord[0] + 1 < self.board_size:  # down
            adjacents_coords.append((self.coord[0] + 1, self.coord[1]))
        if self.coord[1] - 1 >= 0:  # left
            adjacents_coords.append((self.coord[0], self.coord[1] - 1))
        
        return adjacents_coords


class Board:
    def __init__(self, size):
        self.size = size
        counter = count(0)
        self.board = [[Tile(next(counter), size) for _ in range(size)] for _ in range(size)]
        self.emptyTile:Tile = self.board[0][0]

    def getPossibleMovements(self):
        return self.emptyTile.getAdjacentsCoords()
    
    def makeMove(self, move_coord):
        tile_to_move:Tile = self.board[move_coord[0], move_coord[1]]
        adjacents_tile_to_move = tile_to_move.getAdjacentsCoords()
        for adj in adjacents_tile_to_move:
            adj_:Tile = adj
            if adj_.isEmptyTile:
                coord_mask = (adj_.coord[0], adj_.coord[1])
                adj_.coord[0] = tile_to_move.coord[0]
                adj_.coord[1] = tile_to_move.coord[1]

                tile_to_move.coord[0] = coord_mask[0]
                tile_to_move.coord[1] = coord_mask[1]

                self.board[move_coord[0]][move_coord[1]] = adj_
                self.board[adj_.coord[0]][adj_.coord[1]] = tile_to_move

                return True
        
        return False
                
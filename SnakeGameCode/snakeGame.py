#TODO this is where the code going for the game
import pygame
from pygame.locals import *


class Snake_Game:
    def __init__(self) -> None:
        self.game_over = False
        pygame.init()
        size = (width, height) = 800, 800
        self.window = pygame.display.set_mode(size)
    def drawGrid(self):
        blockSize = 40 #Set the size of the grid block
        for x in range(0, 800, blockSize):
            for y in range(0, 800, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.window, (200,200,200), rect, 1)


if __name__ == "__main__":
    game = Snake_Game()
    game.drawGrid()


    while game.game_over == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    print("left")
                if event.key == K_RIGHT:
                    print("right")
                if event.key == K_UP:
                    print("up")
                if event.key == K_DOWN:
                    print("down")
            elif event.type == QUIT:
                game.game_over = True
        pygame.display.flip()


import pygame
import time
from pygame.locals import *
class Snake_Game:
    def __init__(self) -> None:
        self.game_over = False
        pygame.init()
        size = (width, height) = 800, 800
        self.window = pygame.display.set_mode(size)
        self.snake = Snake(self.window, 5, 40)
        self.snake.draw()

    def drawGrid(self): #function to create grid
        blockSize = 40 #Set the size of the grid block
        for x in range(0, 800, blockSize): #starting from 0 to 800 increase by blockSize every iteration
            for y in range(0, 800, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.window, (200,200,200), rect, 1)
    
    def play(self):
        self.snake.Snake_Movement()
    
    def Run_Game(self):
        game.drawGrid()

        while game.game_over == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        print("left")
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        print("right")
                        self.snake.move_right()
                    if event.key == K_UP:
                        print("up")
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        print("down")
                        self.snake.move_down()
                elif event.type == QUIT:
                    game.game_over = True
            self.window.fill((0, 0, 0))
            game.drawGrid()
            self.play()
            time.sleep(.2)
            pygame.display.flip()

class Snake:
    def __init__(self, window, length, blockSize):
        self.length = length
        self.image = pygame.image.load("SnakeGameCode/pictures/block.jpg").convert()
        self.Game_Screen = window
        self.direction = 'right'
        self.x = [40] * length
        self.y = [40] * length
        self.blockSize = blockSize

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def Snake_Movement(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= self.blockSize
        if self.direction == 'right':
            self.x[0] += self.blockSize
        if self.direction == 'up':
            self.y[0] -= self.blockSize
        if self.direction == 'down':
            self.y[0] += self.blockSize

        self.draw()

    def draw(self):
        #self.Game_Screen.fill((110, 110, 5))

        for i in range(self.length):
            self.Game_Screen.blit(self.image, (self.x[i], self.y[i]))
            print(i)
        pygame.display.flip()

    def increase_Snakelength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


if __name__ == "__main__":
    game = Snake_Game()
    game.Run_Game()

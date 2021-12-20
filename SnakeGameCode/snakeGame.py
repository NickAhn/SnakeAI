
import pygame
import time
from pygame.locals import *
import random 

class Snake_Game:
    def __init__(self) -> None:
        self.score = 0
        self.game_over = False
        self.fruit_dict = {}
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

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + 40:
            if y1 >= y2 and y1 < y2 + 40:
                return True
        return False

    def play(self):
        self.snake.Snake_Movement()

        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"
    
    def Run_Game(self):
        self.drawGrid()
        snake_direction = 'R'

        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT and snake_direction != 'R':
                        # print("left")
                        self.snake.move_left()
                        snake_direction = 'L'
                    if event.key == K_RIGHT and snake_direction != 'L':
                        # print("right")
                        self.snake.move_right()
                        snake_direction = 'R'
                    if event.key == K_UP and snake_direction != "D":
                        # print("up")
                        self.snake.move_up()
                        snake_direction = 'U'
                    if event.key == K_DOWN and snake_direction != 'U':
                        # print("down")
                        self.snake.move_down()
                        snake_direction = 'D'
                elif event.type == QUIT:
                    game.game_over = True

            self.boundary_check(self.snake.get_head_location())
            self.window.fill((0, 0, 0))
            self.drawGrid()
            self.play()
            
            self.add_fruit()
            self.draw_fruit()
            self.snake_collision_with_fruit(self.snake.get_head_location())
            
            time.sleep(.2)
            pygame.display.flip()
        
        self.window.fill((255, 255, 255))
        
            
    def add_fruit(self):
        random_int = random.randint(0, 800)
        if random_int % 40 == 0: #! Change the modulus to alter random spawning rate
            x_coord = random.randint(0,20) * 40
            y_coord = random.randint(0,20) * 40
            self.fruit_dict[(x_coord, y_coord)] = pygame.Rect(x_coord, y_coord, 40, 40)

    def draw_fruit(self):
        for fruit in self.fruit_dict.values():
            pygame.draw.rect(self.window, (255,0,0), fruit)
    
    def snake_collision_with_fruit(self, snake_coords):
        try:
            self.fruit_dict.pop((snake_coords[0], snake_coords[1]))
            self.snake.increase_Snakelength()
            self.score += 1
            print(f"Score: {self.score}")
        except:
            pass
            
        # for fruit_coords in self.fruit_dict.keys():
        #     if (fruit_coords[0] == snake_coords[0]) and (fruit_coords[1] == snake_coords[1]):
        #         self.fruit_dict.pop((fruit_coords[0], fruit_coords[1]))
        #         self.snake.increase_Snakelength()
        #         break
        
    def boundary_check(self, snake_coords):
        if snake_coords[0] < 0 or snake_coords[0] > 800 or snake_coords[1] < 0 or snake_coords[1] > 800:
            self.game_over = True

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
        for i in range(self.length-1,0,-1): #for loop that updates where the snake body part is at on screen
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
        for i in range(self.length): #for loop for length of snake
            self.Game_Screen.blit(self.image, (self.x[i], self.y[i])) #draws the image onto screen/grid
            # print(i)
        pygame.display.flip()

    def increase_Snakelength(self): #this will be for when snake eats an apple
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def get_head_location(self):
        return [self.x[0], self.y[0]] #returns snake's head location

if __name__ == "__main__":
    game = Snake_Game()
    game.Run_Game()

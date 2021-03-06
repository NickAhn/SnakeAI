
import pygame
import time
from pygame.locals import *
import random 
import Constants

class Snake_Game:
    def __init__(self) -> None:
        self.score = 0
        self.game_over = False
        self.fruit_dict = {}
        pygame.init()
        size = (width, height) = Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT
        self.window = pygame.display.set_mode(size)
        self.snake = Snake(self.window, 5, 40)
        self.snake.draw_Snake()
        self.fruit_on_screen = False

    def Display_Score(self):
        font = pygame.font.SysFont('comic sans', 30)
        score = font.render(f"Score: {self.score}", True, (200,200,200))
        self.window.fill((0,0,0))
        self.window.blit(score,(650,10))


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
        self.Display_Score()
        self.boundary_check(self.snake.get_head_location())
        self.snake_collision_with_fruit(self.snake.get_head_location())
        if self.fruit_on_screen == False:
            self.add_fruit(self.snake.get_body_coordinates())
        self.draw_fruit()

        if self.fruit_on_screen == False:
            self.add_fruit(self.snake.get_body_coordinates())
        self.draw_fruit()
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print("Collsion")
                raise "Collision Occurred"

    def Losing_Screen(self): #screen for when player loses
        pygame.display.flip()
        self.window.fill((0,0,0))
        font = pygame.font.SysFont('comic sans', 20)
        score_line = font.render(f"Game is over! Your score is {self.score}", True, (200,200,200))
        self.window.blit(score_line, (100,300))
        option_line = font.render(f"To leave game, press Esc. To play again, press Enter!", True, (200,200,200))
        self.window.blit(option_line, (100,500))
        pygame.display.flip()

    def Reset_Game(self): #fills the board reset score and snake
        self.window.fill((0,0,0))
        self.score = 0
        self.snake = Snake(self.window, 5, 40)

    def Run_Game(self):
        snake_direction = 'R'
        Pause_Game = False
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #if esc is hit, then game quits
                        self.game_over = True
                    if event.key == K_RETURN: #stops the "pause" so game plays again
                        Pause_Game = False

                    if not Pause_Game:
                        if event.key == K_LEFT and snake_direction != 'R':
                            self.snake.move_left()
                            snake_direction = 'L'
                        if event.key == K_RIGHT and snake_direction != 'L':
                            self.snake.move_right()
                            snake_direction = 'R'
                        if event.key == K_UP and snake_direction != "D":
                            self.snake.move_up()
                            snake_direction = 'U'
                        if event.key == K_DOWN and snake_direction != 'U':
                            self.snake.move_down()
                            snake_direction = 'D'

                elif event.type == QUIT:
                    self.game_over = True


            try: #this so that we can handle the collsion exception in our way instead of having the game close
                if not Pause_Game:
                    self.play()
            except Exception: #when an exception that occurs (which should be collision) then stop the game so it won't fill the screen through the while loop and display the losing screen
                self.Losing_Screen()
                Pause_Game = True
                self.Reset_Game()

            time.sleep(.25)

        
            
    def add_fruit(self, body_coordinates): 
        spawned_fruit = False
        while spawned_fruit == False:
            x_coord = random.randint(0,19) * 40
            y_coord = random.randint(0,19) * 40
            flag = False
            for segment in body_coordinates:
                if (x_coord == segment[0] and y_coord == segment[1]):
                    flag = True
                    break
            if flag == False:
                self.fruit_dict[(x_coord, y_coord)] = pygame.Rect(x_coord, y_coord, 40, 40)
                self.fruit_on_screen = True
                break
                    

    def draw_fruit(self):
        for fruit in self.fruit_dict.values():
            pygame.draw.rect(self.window, (255,0,0), fruit)
    
    def snake_collision_with_fruit(self, snake_coords):
        try:
            self.fruit_dict.pop((snake_coords[0], snake_coords[1]))
            self.snake.increase_Snakelength()
            self.score += 1
            self.fruit_on_screen = False
            
        except:
            pass
        
    def boundary_check(self, snake_coords):
        if snake_coords[0] < 0 or snake_coords[0] > 800 or snake_coords[1] < 0 or snake_coords[1] > 800:
            print("Collsion")
            raise "Collision Occurred"

class Snake:
    def __init__(self, window, length, blockSize):
        self.length = length
        self.image = pygame.image.load("SnakeGameCode/pictures/block.jpg").convert()
        self.Game_Screen = window
        self.direction = 'right'
        self.x = [40] * length
        self.y = [40] * length
        self.blockSize = blockSize
        self.body_segment_coords = []

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def Snake_Movement(self): 
        self.body_segment_coords = []
        for i in range(self.length-1,0,-1): #for loop that updates where the snake body part is at on screen
            last_body_part = pygame.Rect(self.x[i], self.y[i], 40, 40) # fills in last body segment 
            pygame.draw.rect(self.Game_Screen, (0,0,0), last_body_part)
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            self.body_segment_coords.append((self.x[i], self.y[i]))
        
        # update head
        if self.direction == 'left':
            self.x[0] -= self.blockSize
        if self.direction == 'right':
            self.x[0] += self.blockSize
        if self.direction == 'up':
            self.y[0] -= self.blockSize
        if self.direction == 'down':
            self.y[0] += self.blockSize

        self.draw_Snake()
        

    def draw_Snake(self):
        for i in range(self.length): #for loop for length of snake
            self.Game_Screen.blit(self.image, (self.x[i], self.y[i])) #draws the image onto screen/grid
        pygame.display.flip()

    def increase_Snakelength(self): #this will be for when snake eats an apple
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def get_head_location(self):
        return [self.x[0], self.y[0]] #returns snake's head location
    
    def get_body_coordinates(self):
        return self.body_segment_coords

if __name__ == "__main__":
    game = Snake_Game()
    game.Run_Game()

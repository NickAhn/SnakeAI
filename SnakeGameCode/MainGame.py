from Menu import *
from SnakeGame import *
import Constants


class MainGame:
    def __init__(self, width, height):
        # pygame.init()
        self.size = width, height = Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT
        self.screen = pygame.display.set_mode(size=self.size)

        self.state = 'menu_state'
        
        self.menu_screen = Menu(self)       
        self.state_manager()
        
    
    # Function to manage different states of the screen during while loop
    def state_manager(self):
        if self.state == 'menu_state':  #TODO: create Enums for the state names
            self.menu_screen.run()
        if self.state == 'game_state':  #TODO: create Enums for the state names
            self.game_state()
            
    def game_state(self):
        game = Snake_Game()
        game.Run_Game()
            
    

#! TESTING
pygame.init()       
test = MainGame(WINDOW_WIDTH, WINDOW_HEIGHT)
while True:
    # print(test.state)
    test.state_manager()
    pygame.display.update()
        
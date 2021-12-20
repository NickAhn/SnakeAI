from Menu import *
from SnakeGame import *

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800

class MainGame:
    def __init__(self, width, height):
        # pygame.init()
        fullscreen = False
        self.size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.screen = None
        if fullscreen == False:
            self.screen = pygame.display.set_mode(size=self.size)
        else:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            
        self.state = 'menu_state'
            
        self.menu_screen = Menu(self)
        # self.game_screen = Snake_Game()
        
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
            
    
            
pygame.init()       
test = MainGame(WINDOW_WIDTH, WINDOW_HEIGHT)
while True:
    # print(test.state)
    test.state_manager()
    pygame.display.update()
        
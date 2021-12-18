from Menu import *

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480

class mainGame:
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
        # self.game_Screen = Snake_Game()
        
        self.state_manager()
        
    
    # Function to manage different states of the screen during while loop
    def state_manager(self):
        if self.state == 'menu_state':  #TODO: create Enums for the state names
            self.menu_screen.run()
        if self.state == 'game_state':  #TODO: create Enums for the state names
            self.game_state()
            
    def game_state(self):
        #! this is a test
        self.screen = self.screen
        self.screen.fill(color=(255, 0, 0))
        
        events = pygame.event.get()
        for event in events:
            # print(f"Event: {event}")
            if event.type == pygame.QUIT:
                print("QUIT GAME ")
                pygame.quit()
                run = False
                # sys.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'menu_state'
            
    
            
pygame.init()       
test = mainGame(WINDOW_WIDTH, WINDOW_HEIGHT)
while True:
    print(test.state)
    test.state_manager()
    pygame.display.updte
        
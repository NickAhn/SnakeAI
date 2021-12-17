import os
from typing import Text
import pygame
from pygame import color
from pygame.constants import FULLSCREEN, SCRAP_SELECTION
import pygame_widgets
from pygame_widgets.button import Button
import menu
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480
class mainGame:
    button_Color_Inactive = (221, 231, 238)
    button_Color_Clicked = (221, 231, 238)
    button_Color_Hover = (216, 210, 205)
    size = None
    
    def __init__(self, fullscreen=False ) -> None:
        pygame.init()
        self.size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT
        
        self.screen = None
        if fullscreen == False:
            self.screen = pygame.display.set_mode(size=self.size)
        else:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        mainGame.size = self.size
        
        mainGame.addButtons(screen=self.screen)
        
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    print("QUIT GAME ")
                    pygame.quit()
                    run = False
                    quit()
                    
            pygame_widgets.update(events)
            pygame.display.update()
            
    
    def addButtons(screen:pygame.display):
        """Adds buttons to main menu screen
        Args:
            screen (pygame.display): takes main menu pygame display
        """
        
        screen.fill(color=(255, 255, 255))
        
        play_button = Button(win=screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT-250, width=100, height=35,
                             text="Play without AI", 
                             onClick=print("Clicked Play without AI"), #! Add Function to play game w/o AI
                             inactiveColour=mainGame.button_Color_Inactive,
                             hoverColour=mainGame.button_Color_Hover,
                             pressedColour=mainGame.button_Color_Clicked)
        
        select_AI = Button(win=screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT -200, width=100, height=35,
                           text="Select AI", 
                           onClick=print("Clicked Select AI"), #! Add Function Call to switch to AI switcher screen
                           inactiveColour=mainGame.button_Color_Inactive,
                           hoverColour=mainGame.button_Color_Hover,
                           pressedColour=mainGame.button_Color_Clicked)
        
        play_AI = Button(win=screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT -150, width=100, height=35,
                         text="Play With AI", 
                         onClick=print("Clicked Play with AI"), #! Add Funciton Call to switch to gameplay w AI
                         inactiveColour=mainGame.button_Color_Inactive,
                         hoverColour=mainGame.button_Color_Hover,
                         pressedColour=mainGame.button_Color_Clicked)
        
        quit_button = Button(win=screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT-100, width=100, height=35,
                             text="Quit Game",
                             onClick=pygame.QUIT,
                             inactiveColour=mainGame.button_Color_Inactive,
                             hoverColour=mainGame.button_Color_Hover,
                             pressedColour=mainGame.button_Color_Clicked)
        
        
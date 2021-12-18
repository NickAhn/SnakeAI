import os
from typing import Text
import pygame
from pygame import color
from pygame.constants import FULLSCREEN, MOUSEBUTTONDOWN, SCRAP_SELECTION
import pygame_widgets
from pygame_widgets.button import Button, ButtonArray
from snakeGame import Snake_Game, Snake
import menu
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480
class menu:
    button_Color_Inactive = (221, 231, 238)
    button_Color_Clicked = (221, 231, 238)
    button_Color_Hover = (216, 210, 205)
    size = None
    screen = None
    def __init__(self, fullscreen=False):
        pygame.init()
        self.size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT

        self.game = Snake_Game()

        self.screen = None
        if fullscreen == False:
            self.screen = pygame.display.set_mode(size=self.size)
        else:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        
        # menu.size = size
        self.screen = self.screen
        self.screen.fill(color=(255, 255, 255))
        
        play_button = Button(win=self.screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT-250, width=100, height=35,
                             text="Play without AI", 
                             onClick=lambda: self.game.Run_Game() ,#print("Clicked Play without AI"), #! Add Function to play game w/o AI
                             inactiveColour=menu.button_Color_Inactive,
                             hoverColour=menu.button_Color_Hover,
                             pressedColour=menu.button_Color_Clicked)
        
        select_AI = Button(win=self.screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT -200, width=100, height=35,
                           text="Select AI", 
                           onClick=lambda: self.testFunction(),
                           inactiveColour=menu.button_Color_Inactive,
                           hoverColour=menu.button_Color_Hover,
                           pressedColour=menu.button_Color_Clicked)
        
        play_AI = Button(win=self.screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT -150, width=100, height=35,
                         text="Play With AI", 
                         onClick=lambda: print("Clicked Play with AI"), #! Add Funciton Call to switch to gameplay w AI
                         inactiveColour=menu.button_Color_Inactive,
                         hoverColour=menu.button_Color_Hover,
                         pressedColour=menu.button_Color_Clicked)
        
        quit_button = Button(win=self.screen, x=WINDOW_WIDTH/2 - 50, y=WINDOW_HEIGHT-100, width=100, height=35,
                             text="Quit Game",
                             onClick=pygame.QUIT,
                             inactiveColour=menu.button_Color_Inactive,
                             hoverColour=menu.button_Color_Hover,
                             pressedColour=menu.button_Color_Clicked)
        
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                print(f"Event: {event}")
                if event.type == pygame.QUIT:
                    print("QUIT GAME ")
                    pygame.quit()
                    run = False
                    quit()
                # elif event.type == pygame.MOUSEBUTTONDOWN and 
            pygame_widgets.update(events)
            pygame.display.update()
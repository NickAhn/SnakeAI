import os
import pygame
import menu


# Window Creation

if __name__ == "__main__":
    pygame.init()
    size = width, height = 480, 480
    screen = pygame.display.set_mode(size=size)
    pygame.display.set_caption("Snake Game AI")
    color = (255, 255, 255) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        #! Do not run or else it'll cause an infinite loop
        
# TODO: Switch Window Focus to newly created window

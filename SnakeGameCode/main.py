from menu import *



# Window Creation
if __name__ == "__main__":
<<<<<<< HEAD
    mainGame(fullscreen=False)
=======
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
>>>>>>> 65b7bef3908120042907f77e207237fe4a527a46
        

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

cook = pygame.image.load("Cookie.png").convert_alpha()



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    cook = pygame.transform.rotate(cook)
    screen.blit(cook, (400, 120))
    #if cookie_count >= price:
        #buy power_up
        #powerup_enabled = true

    #power_up could be +2 cookie per click 
        #everytime you buy the upgrade it gets more expensive but makes it +3 +4 etc
        #power_up it auto clicks for you so you get +1 a sec for doing nothing this also gets more expensive buy you get +2 +3 +4 etc
        #you have to get to a million to buy the last pawer up which just ends the game 

    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    clock.tick(144)  # limits FPS

pygame.quit() 
# Import libraries
import pygame, asyncio

# pygame init
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Import other scripts
import cookiebehavior as cookie

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # Rotate cookie
    asyncio.run(cookie.cookiebehavior.cookierotate(cookie, screen=screen))
    

    #if cookie_count >= price:
        #buy power_up
        #powerup_enabled = true

    #power_up could be +2 cookie per click 
        #everytime you buy the upgrade it gets more expensive but makes it +3 +4 etc
        #power_up it auto clicks for you so you get +1 a sec for doing nothing this also gets more expensive buy you get +2 +3 +4 etc
        #you have to get to a million to buy the last pawer up which just ends the game 

    pygame.display.flip()
    clock.tick(120)

pygame.quit() 
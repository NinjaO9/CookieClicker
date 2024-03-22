# Import libraries
import pygame, asyncio

# pygame init
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Game related objects
cookieimg = pygame.image.load("Cookie.webp") #.convert_alpha()
cookierect = cookieimg.get_rect(center=(640, 360))
score = 0
player_mouse = pygame.mouse

# Import other scripts
import cookiebehavior as cookie
Cbehavior = cookie.Cbehavior # Let the class easily be called


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#2d72cd")

    # Rotate cookie
    asyncio.run(Cbehavior.cookierotate(cookie, screen=screen, cookieimg=cookieimg))

    asyncio.run(Cbehavior.cookiedebug(cookie, screen=screen, cookieimg=cookieimg))
    
     

    if event.type == pygame.MOUSEBUTTONDOWN:
        if (cookierect.topleft[0] < player_mouse.get_pos()[0] < cookierect.topright[0]):
            score += score
            print(score)




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
# Import libraries---------------
import pygame, asyncio

# pygame init
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Game related objects------------
cookieimg = pygame.image.load("Cookie.webp").convert_alpha() # init cookie image
cookierect = cookieimg.get_rect(center=(640, 360)) # Create cookieimg rectangle to make it easier to call
cookie_count = 0 # Current count of cookies
autocookiemulti = 1 # Current multiplier for auto cookies
angle = 0
player_mouse = pygame.mouse # Player's mouse
pressed = False # Object to track if the mouse has been pressed and released
press_multiplier = 1 # How many cookies per click

# Import other scripts----------------
import cookiebehavior

CBehavior = cookiebehavior.Cbehavior(screen, cookieimg, angle, cookie_count) # Let the class easily be called

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#2d72cd")

    asyncio.run(CBehavior.cookierotate()) # Rotate cookie

    if event.type == pygame.MOUSEBUTTONDOWN or pressed == True: # Clicking cookie
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed == True:
            if (cookierect.topleft[0] < player_mouse.get_pos()[0] < cookierect.topright[0]):
                cookie_count += press_multiplier
                pressed = False
                print(cookie_count)
    
    
    #if cookie_count >= price:
            #buy power_up
            #powerup_enabled = true
                    

    #if cookie_count >= price
    #buy power_up
    #cookie_count x press_multiplier +1

    #if cookie_count >= price
    #buy power_up
    #cookie_count x autocookiemulti +1

    #power_up could be +2 cookie per click 
        #everytime you buy the upgrade it gets more expensive but makes it +3 +4 etc
        #power_up it auto clicks for you so you get +1 a sec for doing nothing this also gets more expensive buy you get +2 +3 +4 etc
        #you have to get to a million to buy the last pawer up which just ends the game 

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 
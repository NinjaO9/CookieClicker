# Import libraries---------------
import pygame, asyncio

# pygame init--------------------
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font('freesansbold.ttf', 32)

# Game related objects-------------
cookieimg = pygame.image.load("Cookie.webp").convert_alpha() # init cookie image
cookierect = cookieimg.get_rect(center=(640, 360)) # Create cookieimg rectangle to make it easier to call
autocookiemulti = 1 # Current multiplier for auto cookies
angle = 0
player_mouse = pygame.mouse # Player's mouse
pressed = False # Object to track if the mouse has been pressed and released
press_multiplier = 1 # How many cookies per click

power_ups = ["Grandma", "Baker", "Oven"]

pygame.display.set_icon(cookieimg)
pygame.display.set_caption("Clicking cookies...")


# Import other scripts----------------
import cookiebehavior
import powerup

CBehavior = cookiebehavior.Cbehavior(screen, cookieimg, angle) # Let the class easily be called
PowerUp = powerup.PowerUps(autocookiemulti, press_multiplier, power_ups)

# Background functions-----------------
async def background() -> None:
    text = font.render(f"Cookies: {PowerUp.cookiecount}", True, (0,0,0))
    screen.blit(text, (500, 50))
    await CBehavior.cookierotate()

# Main Program-------------------------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#2d72cd")

    asyncio.run(background()) # Do whatever needs to be done in the background

    if event.type == pygame.MOUSEBUTTONDOWN or pressed: # Clicking cookie
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed:
            if (cookierect.topleft[0] < player_mouse.get_pos()[0] < cookierect.topright[0]):
                PowerUp.cookiecount += press_multiplier
                pressed = False
        
    press_multiplier = PowerUp.applypowerup(press_multiplier)

    #you have to get to a million to buy the last pawer up which just ends the game 
    
    pygame.display.flip()
    clock.tick(60)

# TODO: Make an option to buy a power up, rather than forcing the user to get it automatically
# TODO: Increase the price requirements for a power up, go over how it should be incremented (Probably by being squared)
# TODO: Create a way for cookie counter to go up each second without affecting the speed of the other files
# TODO: Figure out how to implement other power ups into the powerup.py file
# TODO: Create the GUI for the player to interact with, allowing them to buy whatever powerups they want
# TODO: Create an end goal / create a 'reward' or something when the player reaches 1 million cookies
    
# OPTIONAL------
# TODO: Create mini cookies that give the player a static amount of cookies. This could maybe be a powerup

pygame.quit() 
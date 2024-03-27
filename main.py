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
price = 50
player_mouse = pygame.mouse # Player's mouse
pressed = False # Object to track if the mouse has been pressed and released
power_ups = ["Grandma", "Baker", "Oven"]

pygame.display.set_icon(cookieimg)
pygame.display.set_caption("Clicking cookies...")


# Import other scripts----------------
import cookiebehavior
import powerup

CBehavior = cookiebehavior.Cbehavior(screen, cookieimg, angle) # Let the class easily be called
Hands = powerup.PowerUps(autocookiemulti, price)

for power in power_ups:
    price *= 3
    power = powerup.PowerUps(autocookiemulti, price)

# Background functions-----------------
async def background() -> None:
    text = font.render(f"Cookies: {Hands.cookiecount}", True, (0,0,0))
    dtext = font.render(f"Price: {Hands.price}", True, (0,0,0))
    screen.blit(text, (500, 50))
    screen.blit(dtext, (200, 50))
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
                Hands.cookiecount += Hands.pressmulti
                pressed = False

    if pygame.key.get_pressed()[pygame.K_p]:
        Hands.applypresspowerup()
        
    pygame.display.flip()
    clock.tick(60)

# TODO: Make an option to buy a power up, rather than forcing the user to get it automatically
# TODO: Create a way for cookie counter to go up each second without affecting the speed of the other files
# TODO: Figure out how to implement other power ups into the powerup.py file
# TODO: Create the GUI for the player to interact with, allowing them to buy whatever powerups they want
# TODO: Create an end goal / create a 'reward' or something when the player reaches 1 million cookies
    
# OPTIONAL------
# TODO: Create mini cookies that give the player a static amount of cookies. This could maybe be a powerup

pygame.quit() 
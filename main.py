# Import libraries---------------
import pygame
from pygame import mouse, key, display

# pygame init--------------------
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
screen = display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Game related objects-------------
cookieimg = pygame.image.load("Cookie.webp").convert_alpha()
cookierect = cookieimg.get_rect(center=(340, 360)) 
atime = 0
price = 50
power_ups= []
display.set_icon(cookieimg)
display.set_caption("Clicking cookies...")
power_names= (("Grandma", 1), ("Baker", 3), ("Oven", 5)) # If more power ups are going to be added, edit this list. Format it this way: (Name, auto increment)

# Import other scripts----------------
from cookiebehavior import Cbehavior
from powerup import PowerUps

CBehavior = Cbehavior(screen, cookieimg) 
Hands = PowerUps(price, "Hands", None)

for pname, automulti in power_names:
    price *= 3.5
    price = int(price)
    power = PowerUps(price, pname, automulti)
    print(power.__dict__) # Debugging purposes. Delete when everything is ready
    power_ups.append(power)

if len(power_ups) == len(power_names):
    pressed = False 
    running = True
    print("The current powers are: ")
    for power in power_ups: #Debugging. Remove when done and ready to submit
        print(f"Power: {power.name} Starting Multiplier: {power.automulti}") 
else:
    print("An Error Occured! (length of power_ups != length of power_names)")

# Background functions-----------------
    
def background() -> None:
    tempy = 50
    screen.fill("#2d72cd")
    count = font.render(f"Cookies: {PowerUps.cookiecount}", True, (0,0,0))
    pPrice = font.render(f"Press Price: {Hands.price}", True, (0,0,0))
    screen.blit(count, (250,tempy))
    screen.blit(pPrice, (900, tempy)) 
    for power in power_ups:
        tempy += 50
        screen.blit(font.render(f"{power.name} Price: {power.price}", True, (0,0,0)), (900, tempy))
    
# Main Program-------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    background()
    CBehavior.cookierotate()

    if event.type == pygame.MOUSEBUTTONDOWN or pressed:
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed:
            if (cookierect.topleft[0] < mouse.get_pos()[0] < cookierect.bottomright[0]) and (cookierect.topleft[1] < mouse.get_pos()[1] < cookierect.bottomright[1]):
                PowerUps.cookiecount += PowerUps.pressmulti
                pressed = False

    if key.get_pressed()[pygame.K_p]:
        Hands.checkpurchasereqs(True)
    if key.get_pressed()[pygame.K_o]:
        power_ups[0].checkpurchasereqs(False)
    if key.get_pressed()[pygame.K_i]:
        power_ups[1].checkpurchasereqs(False)
    if key.get_pressed()[pygame.K_u]:
        power_ups[2].checkpurchasereqs(False)
    if key.get_pressed()[pygame.K_RCTRL]:
        PowerUps.cookiecount += 100
                
    display.flip()
    dt = clock.tick(60)/1000
    atime += dt
    if atime >= 1:
        PowerUps.getautocookie()
        display.set_caption(f"Clicking cookies... {PowerUps.cookiecount}")
        atime = 0

pygame.quit() 

# TODO: Create the GUI for the player to interact with, allowing them to buy whatever powerups they want
# TODO: Create an end goal / create a 'reward' or something when the player reaches 1 million cookies
    
# OPTIONAL------
# TODO: Create mini cookies that give the player a static amount of cookies. This could maybe be a powerup

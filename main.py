# Import libraries---------------
import pygame

# pygame init--------------------
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Game related objects-------------
cookieimg = pygame.image.load("Cookie.webp").convert_alpha()
cookierect = cookieimg.get_rect(center=(640, 360)) 
price = 50
pressed = False 
power_ups= []
pygame.display.set_icon(cookieimg)
pygame.display.set_caption("Clicking cookies...")

power_names= ["Grandma", "Baker", "Oven"] # If more power ups are going to be added, edit this list. DO NOT CHANGE THE 'POWER_UPS' LIST

# Import other scripts----------------
import cookiebehavior
import powerup

CBehavior = cookiebehavior.Cbehavior(screen, cookieimg) 
Hands = powerup.PowerUps(price, "Hands")

for power in power_names:
    price *= 3.5
    price = int(price)
    power = powerup.PowerUps(price, power)
    print(power.__dict__) # Debugging purposes. Delete when everything is ready
    power_ups.append(power)

if len(power_ups) == len(power_names):
    running = True
    cycled = False
    print("The current powers are: ")
    for power in power_ups: #Debugging. Remove when done and ready to submit
        print(power.power) 
else:
    print("An Error Occured! (length of power_ups != length of power_names)")

# Background functions-----------------
    
def background() -> None:
    global cycled
    if not cycled:
        #t2.start()
        cycled = True
    text = font.render(f"Cookies: {powerup.PowerUps.cookiecount}", True, (0,0,0))
    dtext = font.render(f"Press Price: {Hands.price}", True, (0,0,0))
    gtext = font.render(f"Gma Price: {power_ups[0].price}", True, (0,0,0))
    screen.blit(text, (500, 50))
    screen.blit(dtext, (200, 50)) 
    screen.blit(gtext, (200, 100)) 

def autocookie() -> None:
    powerup.PowerUps.cookiecount += powerup.PowerUps.automulti
# Main Program-------------------------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#2d72cd")

    CBehavior.cookierotate()
    autocookie()
    background()


    if event.type == pygame.MOUSEBUTTONDOWN or pressed:
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed:
            if (cookierect.topleft[0] < pygame.mouse.get_pos()[0] < cookierect.bottomright[0]) and (cookierect.topleft[1] < pygame.mouse.get_pos()[1] < cookierect.bottomright[1]):
                powerup.PowerUps.cookiecount += powerup.PowerUps.pressmulti
                pressed = False

    if pygame.key.get_pressed()[pygame.K_p]:
        Hands.checkpurchasereqs(True)
    if pygame.key.get_pressed()[pygame.K_o]:
        power_ups[0].checkpurchasereqs(False)
    if pygame.key.get_pressed()[pygame.K_i]:
        power_ups[1].checkpurchasereqs(False)
    if pygame.key.get_pressed()[pygame.K_u]:
        power_ups[2].checkpurchasereqs(False)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit() 

# TODO: Create a way for cookie counter to go up each second without affecting the speed of the other files
# TODO: Figure out how to implement other power ups into the powerup.py file
# TODO: Create the GUI for the player to interact with, allowing them to buy whatever powerups they want
# TODO: Create an end goal / create a 'reward' or something when the player reaches 1 million cookies
    
# OPTIONAL------
# TODO: Create mini cookies that give the player a static amount of cookies. This could maybe be a powerup

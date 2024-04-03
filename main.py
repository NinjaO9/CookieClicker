# Import libraries and scripts---------------
import pygame, time
from pygame import mouse, key, display
from powerup import PowerUps
from objects import *

# Init powerup lists----------------
for pname, automulti in power_names:
    power = PowerUps(price, pname, automulti)
    price *= 3.2
    price = int(price)
    print(power.__dict__) # Debugging purposes. Delete when everything is ready
    power_ups.append(power)

if len(power_ups) == len(power_names):
    running = True
else:
    print("An Error Occured! (length of power_ups != length of power_names)")

# Background functions-----------------
    
def background() -> None:
    tempy = 50
    count = font.render(f"Cookies: {PowerUps.cookiecount}", True, (255,255,255))
    screen.blit(backgrnd, (0,0))
    screen.blit(count, (600,tempy))
    cookierotate()
    for power in power_ups:
        tempy += 50
        screen.blit(font.render(f"{power.name} Price: {power.price}", True, (255,255,255)), (900, tempy))

def cookierotate() -> None:
    global angle
    angle += .1 #Degrees per frame
    cookie = (pygame.transform.rotate(cookieimg, angle))
    cookierect = cookie.get_rect(center=(640, 340))
    screen.blit(cookie, cookierect)

# Main Program-------------------------

display.set_icon(cookieimg)
display.set_caption("Clicking cookies...")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False   
     
    if PowerUps.cookiecount >= 100000:
        running = False
        
    background()

    if showing:
        screen.blit(font.render(f"+{PowerUps.pressmulti}", True, (0,0,0)), (mouse.get_pos()))

    if event.type == pygame.MOUSEBUTTONDOWN or pressed:
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed:
            if (cookierect.topleft[0] < mouse.get_pos()[0] < cookierect.bottomright[0]) and (cookierect.topleft[1] < mouse.get_pos()[1] < cookierect.bottomright[1]):
                PowerUps.cookiecount += PowerUps.pressmulti
                showing = True
                pressed = False

    if key.get_pressed()[pygame.K_p]:
        power_ups[0].checkpurchasereqs(True)
        time.sleep(0.05)
    if key.get_pressed()[pygame.K_o]:
        power_ups[1].checkpurchasereqs(False)
        time.sleep(0.05)
    if key.get_pressed()[pygame.K_i]:
        power_ups[2].checkpurchasereqs(False)
        time.sleep(0.05)
    if key.get_pressed()[pygame.K_u]:
        power_ups[3].checkpurchasereqs(False)
        time.sleep(0.05)
    if key.get_pressed()[pygame.K_RCTRL]:
        PowerUps.cookiecount += 10000

    display.flip()
    dt = clock.tick(60)/1000
    atime += dt
    if atime >= 1:
        PowerUps.getautocookie()
        showing = False
        display.set_caption(f"Clicking cookies... {PowerUps.cookiecount}")
        atime = 0


while PowerUps.cookiecount >= 100000:
    screen.blit(happy, (0,0))
    screen.blit(font.render(f"You did hit 100,000 cookies!", True, (0,0,0)), (640, 340))
    screen.blit(font.render(f"(Manditory crash)", True, (0,0,0)), (640, 440))
    display.flip()

pygame.quit() 

# TODO: Create the GUI for the player to interact with, allowing them to buy whatever powerups they want
# TODO: Create an end goal / create a 'reward' or something when the player reaches 1 million cookies
    
# OPTIONAL------
# TODO: Create mini cookies that give the player a static amount of cookies. This could maybe be a powerup

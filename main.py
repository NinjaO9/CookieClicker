# Import libraries and scripts---------------
import pygame, time
from pygame import mouse, key, display
from powerup import PowerUps
from objects import *

# Init powerup lists----------------
for pname, automulti, letter, pykey in power_names:
    power = PowerUps(price, pname, automulti, letter, pykey)
    price *= 3.2
    price = int(price)
    power_ups.append(power)

if len(power_ups) == len(power_names):
    running = True
else:
    print("An Error Occured! (length of power_ups != length of power_names)")

# Background functions-----------------
    
def background() -> None:
    tempy = 50
    count = font.render(f"Cookies: {PowerUps.cookiecount}", True, WHITE)
    CPS = font.render(f"CPS: {PowerUps.autogain}", True, WHITE)
    screen.blit(backgrnd, (0,0))
    cookierotate()
    screen.blit(count, (550,tempy))
    screen.blit(CPS, (550, 100))
    for power in power_ups:
        tempy += 50
        screen.blit(font.render(f"({power.letter}) {power.name} Price: {power.price}", True, WHITE), (870, tempy))

def cookierotate() -> None:
    global angle
    angle += .1 #Degrees per frame
    cookie = (pygame.transform.rotate(cookieimg, angle))
    cookierect = cookie.get_rect(center=(640, 340))
    screen.blit(cookie, cookierect)

# Main Program-------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False   
        
    background()

    if PowerUps.cookiecount >= 100000:
        screen.blit(font.render(f"You hit 100,000 cookies!", True, WHITE, BLACK), (40, 100))
        cookieimg = happy

    if event.type == pygame.MOUSEBUTTONDOWN or pressed:
        pressed = True
        if event.type == pygame.MOUSEBUTTONUP and pressed:
            if (cookierect.topleft[0] < mouse.get_pos()[0] < cookierect.bottomright[0]) and (cookierect.topleft[1] < mouse.get_pos()[1] < cookierect.bottomright[1]):
                PowerUps.cookiecount += PowerUps.pressmulti
                pressed = False


    if key.get_pressed()[pygame.K_RCTRL]: # Cheat code for debugging
        PowerUps.cookiecount += 10000

    for power in power_ups:
        if key.get_pressed()[power.pykey]:
            ispress = True if power.automulti == None else False
            power.checkpurchasereqs(ispress)
            time.sleep(0.05)


    display.flip()
    dt = clock.tick(60)/1000
    atime += dt
    if atime >= 1:
        PowerUps.getautocookie()
        display.set_caption(f"Clicking cookies... {PowerUps.cookiecount}")
        atime = 0

pygame.quit() 

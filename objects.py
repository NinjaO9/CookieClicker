import pygame 
from pygame import display 
# pygame init
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)
screen = display.set_mode((1280, 720))
clock = pygame.time.Clock()

# images init
backgrnd = pygame.transform.scale(pygame.image.load("Background.jfif"), (1280,720))
cookieimg = pygame.image.load("Cookie.webp").convert_alpha()
happy = pygame.transform.scale(pygame.image.load("Happy.png"), (360, 360)).convert_alpha()

# variables init
cookierect = cookieimg.get_rect(center=(640, 340)) 
pressed = False 
atime = 0
angle = 0
price = 50

WHITE = (255,255,255)
BLACK = (0,0,0)

# powerup init
power_ups= []
power_names= (
    ("Hands", None, "p", pygame.K_p), 
    ("Grandma", 1, "o", pygame.K_o), 
    ("Baker", 3, "i", pygame.K_i), 
    ("Oven", 5, "u", pygame.K_u), 
    ("BIG OVEN", 100, "y", pygame.K_y)
    ) # If more power ups are going to be added, edit this list. Format it this way: (Name, auto increment, letter, and the pygame letter command)


# Window init

display.set_icon(cookieimg)
display.set_caption("Clicking cookies...")

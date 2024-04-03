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
happy = pygame.transform.scale(pygame.image.load("Happi.jpeg"), (1280, 720))

# variables init
cookierect = cookieimg.get_rect(center=(640, 340)) 
showing = False
pressed = False 
atime = 0
angle = 0
price = 50

# powerup init
power_ups= []
power_names= (("Hands", None), ("Grandma", 1), ("Baker", 3), ("Oven", 5), ("Big MAMA", 1000)) # If more power ups are going to be added, edit this list. Format it this way: (Name, auto increment)
import pygame 
from pygame import display 
# pygame init
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)
screen = display.set_mode((1280, 720))
clock = pygame.time.Clock()

# images init
background = pygame.transform.scale(pygame.image.load("Background.jfif"), (1280,720))
cookieimg = pygame.image.load("Cookie.webp").convert_alpha()
happy = pygame.transform.scale(pygame.image.load("Happi.jpeg"), (1280, 720))

# variables init
cookierect = cookieimg.get_rect(center=(640, 340)) 
showing = False
pressed = False 
atime = 0
angle = 0
price = 50

# powerup init
power_ups= []
power_names= (("Hands", None), ("Grandma", 1), ("Baker", 3), ("Oven", 5), ("Big MAMA", 1000)) # If more power ups are going to be added, edit this list. Format it this way: (Name, auto increment)
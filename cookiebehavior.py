import pygame, asyncio

class Cbehavior():

    angle = 0

    def __init__(self, screen, cookieimg):
        self.screen = screen
        self.cookieimg = cookieimg

    async def cookierotate(self) -> None:
        self.angle += .1 #Degrees per frame
        cookie = (pygame.transform.rotate(self.cookieimg, self.angle))
        cookierect = cookie.get_rect(center=(640, 360))
        self.screen.blit(cookie, cookierect)

    



        

    


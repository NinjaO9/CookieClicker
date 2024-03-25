import pygame, asyncio

class Cbehavior():

    def __init__(self, screen, cookieimg, angle, score):
        self.screen = screen
        self.cookieimg = cookieimg
        self.angle = angle
        self.score = score

    async def cookierotate(self) -> None:
        self.angle += .1 #Degrees per frame
        cookie = (pygame.transform.rotate(self.cookieimg, self.angle))
        cookierect = cookie.get_rect(center=(640, 360))
        self.screen.blit(cookie, cookierect)

    async def cookiedebug(self) -> str:
        pass # Maybe work on this

    async def autocookie(self, autocookiemult : int) -> int:
        pass  # Allow the program to add the autocookiemult to score every second without holding up the rest of the program. Probably look into asyncio documentation



        

    


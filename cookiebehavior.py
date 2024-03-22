import pygame

class Cbehavior():
    global angle
    angle = 0 

    async def cookierotate(self, screen : pygame.display, cookieimg : pygame.surface.Surface) -> None:
        self.angle += .1
        cookie = (pygame.transform.rotate(cookieimg, self.angle))
        cookierect = cookie.get_rect(center=(640, 360))
        screen.blit(cookie, cookierect)

    async def cookiedebug(self, screen : pygame.display, cookieimg : pygame.surface.Surface) -> str:
        pass


        

    


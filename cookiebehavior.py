import pygame

class cookiebehavior(pygame.sprite.Sprite):
    global cookieimg, angle
    cookieimg = pygame.image.load("Cookie.webp").convert_alpha()
    angle = 0 

    async def cookierotate(self, screen : pygame.display):
        self.angle += .1
        cookie = (pygame.transform.rotate(self.cookieimg, self.angle))
        cookierect = cookie.get_rect(center=(640, 360))
        screen.blit(cookie, cookierect)

        

    


import pygame
class PowerUps():

    cookiecount = 0
    pressmulti = 1
    autocookiemulti = 0
    autogain = 0

    def __init__(self, price):
        self.price = price

    def increaseprice(self) -> None:
        self.price *= 2

    def applypresspowerup(self) -> int:
        if self.cookiecount >= self.price:
            self.cookiecount -= self.price
            self.pressmulti += 1
            self.increaseprice()

    def applyautocookiemulti(self):
        if self.cookiecount >= self.price:
            self.cookiecount -= self.price
            
        pass
 
class ShopStuff(PowerUps):
    
    def createshop(self):

        pass

    def buying_powerup(self):
        pass


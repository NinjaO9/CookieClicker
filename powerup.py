import time
class PowerUps():

    cookiecount = 0
    pressmulti = 1
    automulti = 0
    autogain = 0

    def __init__(self, price, power):
        self.price = price
        self.power = power

    def increaseprice(self) -> None:
        self.price *= 2

    @classmethod
    def getautocookie(cls) -> None:
        while True:
            print("Running autocookie")
            time.sleep(1)
            cls.cookiecount += cls.automulti
            print("Cookie count updated?")

    @classmethod
    def applypresspowerup(cls) -> None:
        cls.pressmulti += 1
    
    @classmethod
    def applyautopower(cls, self) -> None:
        cls.automulti += self.autogain
    
    def checkpurchasereqs(self, ispress) -> None:
        if PowerUps.cookiecount >= self.price and ispress:
            PowerUps.cookiecount -= self.price
            PowerUps.applypresspowerup()
            self.increaseprice()
        elif PowerUps.cookiecount >= self.price and not ispress:
            PowerUps.cookiecount -= self.price
            PowerUps.applyautopower(self)
            self.increaseprice()

class AutoCookie(PowerUps):
    
    @classmethod
    async def getautocookie(cls) -> None:
        while True:
            print("Running autocookie")
            time.sleep(1)
            cls.cookiecount += cls.automulti
            print("Cookie count updated?")


 
class ShopStuff(PowerUps):
    
    def createshop(self):
        pass

    def buying_powerup(self):
        pass


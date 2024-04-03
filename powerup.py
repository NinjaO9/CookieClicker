class PowerUps():

    cookiecount = 0
    pressmulti = 1
    autogain = 0

    def __init__(self, price, name, automulti):
        self.price = price
        self.name = name
        self.automulti = automulti

    def increaseprice(self, ispress) -> None:
        if ispress:
            self.price *= 2
        else:
            self.price = int(self.price * 2.5)
            self.increaseautomulti()

    def increaseautomulti(self) -> None:
        self.automulti = int(self.automulti * 1.5)
        if self.automulti == 0 or self.automulti == 1:
            self.automulti += 2

    @classmethod
    def getautocookie(cls) -> int:
        cls.cookiecount += cls.autogain
        return cls.cookiecount

    @classmethod
    def applypresspowerup(cls) -> None:
        cls.pressmulti += 1
    
    @classmethod
    def applyautopower(cls, self) -> None:
        cls.autogain += self.automulti
        print(f"New automulti is: {cls.autogain}")
    
    def checkpurchasereqs(self, ispress) -> None:
        if PowerUps.cookiecount >= self.price and ispress:
            PowerUps.cookiecount -= self.price
            PowerUps.applypresspowerup()
            self.increaseprice(True)
        elif PowerUps.cookiecount >= self.price and not ispress:
            PowerUps.cookiecount -= self.price
            PowerUps.applyautopower(self)
            self.increaseprice(False) 



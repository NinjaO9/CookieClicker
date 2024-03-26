
class PowerUps():

    cookiecount = 0
    pressmulti = 1

    def __init__(self, autocookiemulti, pressmulti, power_ups):
        self.autocookiemulti = autocookiemulti
        self.pressmulti = pressmulti 
        self.power_ups  = power_ups

    def applypowerup(self, pressmulti) -> int:
        if self.cookiecount >= 50:
            self.cookiecount -= 50
            return pressmulti + 1
        else:
            return pressmulti

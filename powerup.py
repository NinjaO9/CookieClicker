
class PowerUps():

    def __init__(self, cookiecount, autocookiemulti, pressmulti, power_ups):
        self.cookiecount = cookiecount
        self.autocookiemulti = autocookiemulti
        self.pressmulti = pressmulti 
        self.power_ups  = power_ups

    def applypowerup(self, cookiecount, pressmulti):
        if cookiecount >= 50:
            return cookiecount - 50, pressmulti + 1
        else:
            return cookiecount, pressmulti

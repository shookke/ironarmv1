import lib.Adafruit_PCA9685 as Adafruit_PCA9685

class cMechanics():

    def init(self, leds, **kwargs):
        self.leds = leds #array of pwm addresses
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm_freq = self.pwm.set_pwm_freq(1000)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def boot(self):
        for led in self.leds:
            self.pwm.set_pwm(led, 1, 0)
        
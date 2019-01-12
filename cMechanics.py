import lib.Adafruit_PCA9685 as Adafruit_PCA9685
import board
import neopixel

class cMechanics:

    def __init__(self, pwm, leds, **kwargs):
        self.leds = pixels = neopixel.NeoPixel(board.D21, 30)
        self.pwm = pwm
        self.pwm_freq = self.pwm.set_pwm_freq(1000)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def boot(self):
        pixels = neopixel.NeoPixel(board.D18, 30)
        pixels[0] = (255, 0, 0)
            
        
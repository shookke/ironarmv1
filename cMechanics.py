import adafruit_pca9685
import board
import neopixel

class cMechanics:

    def __init__(self, **kwargs):
        self.leds = pixels = neopixel.NeoPixel(board.D21, 30)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def boot(self):
        self.leds[0] = (0, 255, 0, 255)
            
        
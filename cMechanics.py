import adafruit_pca9685
import board
import neopixel

class cMechanics:

    def __init__(self, **kwargs):
        ORDER = neopixel.RGBW
        self.leds = pixels = neopixel.NeoPixel(board.D21, 2, pixel_order=ORDER)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def boot(self):
        self.leds[0] = (0, 255, 0, 255)
            
        
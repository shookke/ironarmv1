import adafruit_pca9685
import board
import neopixel

class cMechanics:

    def __init__(self, **kwargs):
        ORDER = neopixel.RGBW
        self.leds = neopixel.NeoPixel(board.D21, 2, pixel_order=ORDER)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def boot(self):
        self.leds[0] = (0, 0, 0, 150)
    
    def status(self, batt, charging):
        if batt <= 20:
            self.leds.fill((100, 150, 0, 0))
        if charging:
            while batt != 100:
                for i in range(0, 100):
                    self.leds.fill((i, 0, 0, 0))
                for i in range(100, 0, -1):
                    self.leds.fill((i, 0, 0, 0))    
        else:
            self.leds.fill((0, 0, 0, 150))


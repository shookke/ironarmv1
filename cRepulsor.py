import lib.Adafruit_PCA9685 as Adafruit_PCA9685
import time
from random import random

class cRepulsor:
    def __init__(self, pwm, led):
        self.armed = bool
        self.led = led #pwm address
        self.pwm = pwm
        self.pwm_freq = self.pwm.set_pwm_freq(1000)
        self.LED_max = 255
        self.LED_min = 0
        self.LED_med = 75
        self.flight_mode = bool

    def arm(self):
        self.pwm.set_pwm_freq(1000)
        for i in range(self.LED_min, self.LED_med):
                #print(i)
                self.pwm.set_pwm(self.led, 0, i)
        self.armed = True
    
    def disarm(self):
        self.pwm.set_pwm_freq(1000)
        for i in range(self.LED_med, -1, -1):
                        #print(i)
                        self.pwm.set_pwm(self.led, 0, i)
        self.armed = False
    
    def fire(self):
        self.pwm.set_pwm(4, 0, self.LED_max)
        time.sleep(0.5)
        self.arm()
    
    def flight(self, active):
        self.pwm.set_pwm_freq(1000)
        while self.flight_mode:
            self.pwm.set_pwm(4, 0, self.LED_max)
            time.sleep(random(0.0,0.9))
            self.pwm.set_pwm(4, 0, self.LED_med)
            time.sleep(random(0.0,0.9))

    def isArmed(self):
        if self.armed:
            return True
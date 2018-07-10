import lib.Adafruit_PCA9685 as Adafruit_PCA9685
import time
from random import random

class cMissle:

    def __init__(self, pwm, motor):
        self.armed = bool
        self.motor = motor #pwm address
        self.pwm = pwm
        self.pwm_freq = self.pwm.set_pwm_freq(60)
        self.servo_min = 150
        self.servo_max = 600

    def arm(self):
        self.pwm.set_pwm(self.motor, 0, self.servo_max)
        self.armed = True
    
    def disarm(self):
        self.pwm.set_pwm(self.motor, 0, self.servo_min)
        self.armed = False
    
    def fire(self):
        print('FIRE!')
    
    def isArmed(self):
        if self.armed:
            return True
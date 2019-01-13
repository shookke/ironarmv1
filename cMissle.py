import lib.Adafruit_PCA9685 as Adafruit_PCA9685
import time
from random import random

class cMissle:

    def __init__(self, pwm, motor):
        self.armed = False
        self.motor = motor #pwm address
        self.pwm = pwm #PCA9685
        self.motor = self.pwm.channels[motor]
        self.pwm.frequency = 60
        self.servo_min = 150
        self.servo_max = 600

    def arm(self):
        self.pwm.frequency = 60
        self.led.duty_cycle = self.servo_max
        self.armed = True
    
    def disarm(self):
        self.pwm.frequency = 60
        self.led.duty_cycle = self.servo_min
        self.armed = False
    
    def fire(self):
        if self.armed:
            print('FIRE!')
    
    def isArmed(self):
        if self.armed:
            return True
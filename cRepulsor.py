import lib.Adafruit_PCA9685 as Adafruit_PCA9685
import pygame  
import time
from random import random

pygame.mixer.init()

class cRepulsor:
    def __init__(self, pwm, led):
        self.armed = False
        self.led = led #pwm address
        self.pwm = pwm
        self.pwm_freq = self.pwm.set_pwm_freq(1000)
        self.arming = pygame.mixer.music.load('res/audio/1.ogg')
        self.firing = pygame.mixer.music.load('res/audio/2.ogg')
        self.disarming = pygame.mixer.music.load('res/audio/3.ogg')
        self.LED_max = 255
        self.LED_min = 0
        self.LED_med = 75
        self.flight_mode = False

    def arm(self):
        self.pwm.set_pwm_freq(1000)
        self.arming = pygame.mixer.music.load('res/audio/1.ogg')   
        self.arming.play()
        for i in range(self.LED_min, self.LED_med):
                #print(i)
                self.pwm.set_pwm(self.led, 0, i)
        while self.arming.get_busy() == True:
            continue
        self.armed = True
    
    def disarm(self):
        self.pwm.set_pwm_freq(1000)
        for i in range(self.LED_med, -1, -1):
                        #print(i)
                        self.pwm.set_pwm(self.led, 0, i)
        self.armed = False
    
    def fire(self):
        if self.armed:
            self.pwm.set_pwm(4, 0, self.LED_max)
            time.sleep(0.5)
            self.arm()
    
    def flight(self):
        if self.flight_mode:
            self.pwm.set_pwm_freq(1000)
            self.pwm.set_pwm(4, 0, self.LED_max)
            time.sleep(random())
            self.pwm.set_pwm(4, 0, self.LED_med)
            time.sleep(random())

    def isArmed(self):
        if self.armed:
            return True
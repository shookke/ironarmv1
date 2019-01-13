import adafruit_pca9685
import pygame  
import time
from random import random

pygame.mixer.init()


class cRepulsor:
    def __init__(self, pwm, led):
        self.armed = False
        self.pwm = pwm
        self.led = self.pwm.channels[led]
        self.pwm.frequency = 1000
        self.arming = 'res/audio/1.ogg'
        self.firing = 'res/audio/2.ogg'
        self.disarming = 'res/audio/3.ogg'
        self.LED_max = 0xffff
        self.LED_min = 0
        self.LED_med = 1000
        self.flight_mode = False

    def arm(self):
        self.pwm.frequency = 1000
        pygame.mixer.music.load(self.arming)  
        pygame.mixer.music.set_volume(1.0) 
        pygame.mixer.music.play()
        time.sleep(0.5)
        for i in range(self.LED_min, self.LED_med):
                self.led.duty_cycle = i
                #time.sleep(0.05)
        while pygame.mixer.music.get_busy() == True:
            continue
        self.armed = True
    
    def disarm(self):
        self.pwm.frequency = 1000
        pygame.mixer.music.load(self.disarming)
        pygame.mixer.music.set_volume(1.0)   
        pygame.mixer.music.play()
        time.sleep(0.5)
        for i in range(self.LED_med, -1, -1):
                        #print(i)
                        self.led.duty_cycle = i
                        #time.sleep(0.05)
        while pygame.mixer.music.get_busy() == True:
            continue
        self.armed = False
    
    def fire(self):
        if self.armed:
            pygame.mixer.music.load(self.disarming)   
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            time.sleep(0.5)
            self.led.duty_cycle = self.LED_max
            while pygame.mixer.music.get_busy() == True:
                continue
            #self.arm()
    
    def flight(self):
        if self.flight_mode:
            self.pwm.frequency = 1000
            self.led.duty_cycle = self.LED_max
            time.sleep(random())
            self.led.duty_cycle = self.LED_med
            time.sleep(random())

    def isArmed(self):
        if self.armed:
            return True
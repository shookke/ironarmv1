import adafruit_pca9685
import pygame as pg
import time
from random import random

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)


class cRepulsor:
    def __init__(self, pwm, led):
        self.clock = pg.time.Clock()
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
        pg.mixer.music.load(self.arming)
        pg.mixer.music.set_volume(1.0)
        pg.mixer.music.play()
        for i in range(self.LED_min, self.LED_med):
            self.led.duty_cycle = i
        while pg.mixer.music.get_busy() == True:
            self.clock.tick(2)
        self.armed = True

    def disarm(self):
        self.pwm.frequency = 1000
        pg.mixer.music.load(self.disarming)
        pg.mixer.music.set_volume(1.0)
        pg.mixer.music.play()
        for i in range(self.LED_med, 0, -1):
            self.led.duty_cycle = i
        while pg.mixer.music.get_busy() == True:
            self.clock.tick(2)
        self.armed = False

    def fire(self):
        if self.armed:
            pg.mixer.music.load(self.firing)
            pg.mixer.music.set_volume(1.0)
            pg.mixer.music.play()
            self.led.duty_cycle = self.LED_max
            time.sleep(0.2)
            self.led.duty_cycle = self.LED_med
            while pg.mixer.music.get_busy() == True:
                self.clock.tick(4)

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

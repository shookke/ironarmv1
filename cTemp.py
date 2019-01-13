import adafruit_pca9685
import time

class cTemp:
    def __init__(self, pwm, cooler, *args, **kwargs):
        self.pwm = pwm
        self.cooler = cooler
        self.pwm.frequency = 60

    def cool(self, temp):
        self.pwm.frequency = 60
        while True:
            self.pwm.set_pwm(1, 1, 0)
            time.sleep(temp)
            self.pwm.set_pwm(1, 0, 1)
            time.sleep(temp * 2)
            continue
        print("Finished Cooling.")
    
import open_myo as myo
import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

LED_min = 0
LED_med = 75
LED_max = 255

rep_armed = 0
missle_armed = 0

cooling_time = 3
pulse = 5

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Boot led on.
pwm.set_pwm(2, 1, 0)

def process_emg(emg):
    print(emg)

def process_imu(quat, acc, gyro):
    print(quat)

def process_sync(arm, x_direction):
    print(arm, x_direction)

def process_classifier(pose):
    global missle_armed
    global rep_armed
    prev_pose = None
    timer = 0
    print(pose)
    if (pose == pose.WAVE_OUT):
        prev_pose = pose
        pwm.set_pwm_freq(1000)
        for i in range(LED_min, LED_med):
                #print(i)
                pwm.set_pwm(4, 0, i)
                rep_armed = 1
    elif (pose == pose.FINGERS_SPREAD):
        prev_pose = pose
        if (rep_armed==1):
                pwm.set_pwm(4, 0, LED_max)
                time.sleep(0.5)
                pwm.set_pwm(4, 0, LED_med)
    elif (pose ==pose.FIST):
        prev_pose = pose
        pwm.set_pwm_freq(60)
        if (rep_armed == 0):
                pwm.set_pwm(0, 0, servo_max)
    elif (pose == pose.WAVE_IN):
        prev_pose = pose
        if (missle_armed == 1):
                print("FIRE ZE MISSLES!")
    elif (pose == pose.DOUBLE_TAP):
        i = 0
        pwm.set_pwm_freq(60)
        while (i < pulse):
                pwm.set_pwm(1, 1, 0)
                time.sleep(cooling_time)
                pwm.set_pwm(1, 0, 1)
                time.sleep(cooling_time)
                i += 1
                continue
        print("Finished Cooling.")

    elif (pose == pose.REST):
        time.sleep(1)
        prev_pose = pose
        if (missle_armed == 1):
                pwm.set_pwm_freq(60)
                pwm.set_pwm(0, 0, servo_min)
                missle_armed = 0
        if (missle_armed == 1):
                pwm.set_pwm_freq(60)
                pwm.set_pwm(0, 0, servo_min)
                missle_armed = 0
        if (rep_armed==1):
                for i in range(LED_med, -1, -1):
                        #print(i)
                        pwm.set_pwm(4, 0, i)
                        rep_armed = 0
    else:
        print('no input')

def process_battery(batt):
    print("Battery level: %d" % batt)

def led_emg(emg):
    if(emg[0] > 80):
        myo_device.services.set_leds([255, 0, 0], [128, 128, 255])
    else:
        myo_device.services.set_leds([128, 128, 255], [128, 128, 255])

myo_mac_addr = myo.get_myo()
print("MAC address: %s" % myo_mac_addr)
myo_device = myo.Device()
myo_device.services.sleep_mode(1) # never sleep
myo_device.services.set_leds([128, 128, 255], [128, 128, 255])  # purple logo a$
myo_device.services.vibrate(1) # short vibration
fw = myo_device.services.firmware()
print("Firmware version: %d.%d.%d.%d" % (fw[0], fw[1], fw[2], fw[3]))
batt = myo_device.services.battery()
print("Battery level: %d" % batt)
myo_device.services.emg_filt_notifications()
# myo_device.services.emg_raw_notifications()
myo_device.services.imu_notifications()
myo_device.services.classifier_notifications()
# myo_device.services.battery_notifications()
myo_device.services.set_mode(myo.EmgMode.FILT, myo.ImuMode.DATA, myo.ClassifierMode.ON)
# myo_device.add_emg_event_handler(process_emg)
# myo_device.add_emg_event_handler(led_emg)
#myo_device.add_imu_event_handler(process_imu)
myo_device.add_sync_event_handler(process_sync)
myo_device.add_classifier_event_hanlder(process_classifier)

while True:
    if myo_device.services.waitForNotifications(1):
        continue
    print("Waiting...")


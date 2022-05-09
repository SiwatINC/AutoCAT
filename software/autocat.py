from time import sleep
import cvcat
from kinematics import kinematics

catdevice = kinematics()
#catdevice.mcu.stepper_run_speed(catdevice.ID_AZIMUTH)
while True:
    sleep(1)
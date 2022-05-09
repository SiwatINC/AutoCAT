from random import randint
from turtle import position
from telemetrix import telemetrix
from config import AZIMUTH_DIR,AZIMUTH_STEP,ELEVATION_DIR,ELEVATION_STEP,STEP_PER_DEGREE,STEPPER_ENABLE_PIN
from time import sleep
import time
from perlin_noise import PerlinNoise

class kinematics:
    def __init__(self) -> None:
        try:
            self.mcu = telemetrix.Telemetrix()
        except:
            print("AutoCAT Device not detected!")
            exit()
        self.shake_function = PerlinNoise(octaves=10,seed=randint(a=0,b=2000))
        self.ID_AZIMUTH = self.mcu.set_pin_mode_stepper(interface=1,pin1=AZIMUTH_STEP,pin2=AZIMUTH_DIR)
        self.mcu.set_pin_mode_digital_output(STEPPER_ENABLE_PIN)
        self.mcu.stepper_set_max_speed(self.ID_AZIMUTH, 1000)
        self.mcu.stepper_set_speed(self.ID_AZIMUTH, 1000)
        self.mcu.stepper_set_acceleration(self.ID_AZIMUTH, 800)
        self.mcu.digital_write(pin=STEPPER_ENABLE_PIN,value=0)
        self.home_all()

    def shutdown(self) -> None:
        self.mcu.shutdown()

    # Homing Functions
    def home_azimuth(self) -> None:
        self.mcu.stepper_move(motor_id=self.ID_AZIMUTH,relative_position=-350*STEP_PER_DEGREE)
        self.mcu.stepper_run(motor_id=self.ID_AZIMUTH,completion_callback=self.motion_completion_callback)
        #sleep(5)
        #self.mcu.stepper_set_current_position(motor_id=self.ID_AZIMUTH,position=0)
    def home_all(self) -> None:
        self.home_azimuth()

    # Movement Funtions
    def move_to_position(self,azi:float,elev:float) -> None:
        self.mcu.stepper_move_to(motor_id=self.ID_AZIMUTH,position=azi*STEP_PER_DEGREE)
    def stop(self) -> None:
        self.mcu.stepper_stop(motor_id=self.ID_AZIMUTH)

    def motion_completion_callback(self,data):
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[2]))
        print(f'Run motor {data[1]} completed motion at: {date}.')
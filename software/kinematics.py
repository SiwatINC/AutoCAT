from random import randint
from turtle import position
from telemetrix import telemetrix
from config import AZIMUTH_DIR,AZIMUTH_STEP,ELEVATION_DIR,ELEVATION_STEP,STEP_PER_DEGREE
from time import sleep
from perlin_noise import PerlinNoise
ID_AZIMUTH = 1
ID_ELEVATION = 2
class kinematics:
    def __init__(self) -> None:
        try:
            self.mcu = telemetrix.Telemetrix()
        except:
            print("AutoCAT Device not detected!")
            exit()
        self.shake_function = PerlinNoise(octaves=10,seed=randint(a=0,b=2000))
        self.mcu.set_pin_mode_stepper(interface=1,pin1=AZIMUTH_DIR,pin2=AZIMUTH_STEP,enable=True)
        self.mcu.set_pin_mode_stepper(interface=1,pin1=ELEVATION_DIR,pin2=ELEVATION_STEP,enable=True)
        self.home_all()

    def shutdown(self) -> None:
        self.mcu.shutdown()

    # Homing Functions
    def home_azimuth(self) -> None:
        self.mcu.stepper_move(motor_id=ID_AZIMUTH,relative_position=-350*STEP_PER_DEGREE)
        sleep(5)
        self.mcu.stepper_set_current_position(motor_id=ID_AZIMUTH,position=0)
    def home_elevation(self) -> None:
        self.mcu.stepper_move(motor_id=ID_ELEVATION,relative_position=-350*STEP_PER_DEGREE)
        sleep(5)
        self.mcu.stepper_set_current_position(motor_id=ID_ELEVATION,position=0)
    def home_all(self) -> None:
        self.home_azimuth()
        self.home_elevation()

    # Movement Funtions
    def move_to_position(self,azi:float,elev:float) -> None:
        self.mcu.stepper_move_to(motor_id=ID_AZIMUTH,position=azi*STEP_PER_DEGREE)
        self.mcu.stepper.move_to(motor_id=ID_ELEVATION,position=elev*STEP_PER_DEGREE)
    def stop(self) -> None:
        self.mcu.stepper_stop(motor_id=ID_AZIMUTH)
        self.mcu.stepper_stop(motor_id=ID_ELEVATION)

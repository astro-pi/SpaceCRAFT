#reading orientation data in a loop, if you dont read it fast enough it goes out of sync
from astro_pi import AstroPi
from time import sleep

ap = AstroPi()

ap.set_imu_config(True, True, True)

while(True):
    orientation = ap.get_orientation_degrees()
    print("yaw = {}; pitch = {}; roll = {}".format(orientation["yaw"], orientation["pitch"], orientation["roll"]))

    sleep(0.1)


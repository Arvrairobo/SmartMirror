from camera import *
from ultrasoundhandler import *
from uihandler import *
from powerswitch import *
from cursorhandler import *

import cv2
import numpy as np
import math

bool_light = True
ultra_sound_handler = UltraSoundHandler()
power_switch = PowerSwitch()
camera = Camera(bool_light)
cursor_handler = CursorHandler()
ui_manager = UIManager()

counter = 0
while True:
    counter+=1
    camera.update_values()
    cursor_location = camera.get_cursor()
    ui_manager.update(cursor_location)
    # print str(counter)
    # if counter >100:
    #     ui_manager.end_news()
    #     counter = -500

    k = cv2.waitKey(10)
    if k == 27: # Esc key breaks out of program
        break # break out of program
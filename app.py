from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
for x in range(5):

    click(1250,0) #lootboxes 1185,108 on start/1236,18 after attack/1250,0 after couple attacks
    time.sleep(2)
    click(1408,909)#collect loot
    time.sleep(2)

    click(100,962) #attack1
    time.sleep(2)
    click(100,962) #attack1
    time.sleep(2)

    click(1425,701) #attack2
    time.sleep(10)

    click(332,978) #troop1
    time.sleep(2)


    click(1780,583) #deploytroop
    time.sleep(2)
    click(1780,583) #deploytroop
    time.sleep(0.21)
    click(1780,583) #deploytroop
    time.sleep(0.22)
    click(1780,583) #deploytroop
    time.sleep(0.23)

    click(112,797)#surrender1
    time.sleep(2)
    click(1126,664)#surrender2
    time.sleep(2)
    click(964,910)#returnHome
    time.sleep(2)
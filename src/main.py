import pygame as pg
import random
import pynput
import keyboard

down_arr = ["down.wav","down2.wav","downspace.wav"]
up_arr = ["up.wav","up2.wav","upspace.wav"]

pg.mixer.pre_init(44100, -16, 2, 2**9)
pg.mixer.init()

arr = set()

print("Ctrl+q to quit")

def on_press(key):
    if key not in arr:
        arr.add(key)
        down.fadeout(2)
        down.play()


def on_release(key):
    up.play()
    arr.remove(key)

listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while not keyboard.is_pressed("ctrl+q"):
    i = random.randint(0,2)
    down = pg.mixer.Sound(down_arr[i])
    up = pg.mixer.Sound(up_arr[i])







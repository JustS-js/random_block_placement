from pynput.mouse import Listener, Button
from keyboard import press, release, add_hotkey, press_and_release
from random import random
DO = False


def on_off():
    global DO
    DO = not DO


add_hotkey('-', on_off)


def hook_click(x, y, button, pressed):
    global DO
    if button == Button.right and pressed:
        if DO:
            randomize_click()
        press('u')
    elif button == Button.right:
        release('u')


def randomize_click():
    # 10 - Керамика
    # 9 - Цемент
    # 8 - Чернит
    # 7 - Резной чернит
    r = random() * 100
    if 0 <= r < 60:
        press_and_release(10)
    elif 60 <= r < 90:
        press_and_release(9)
    elif 90 <= r < 97:
        press_and_release(8)
    else:
        press_and_release(7)


with Listener(on_click=hook_click) as listener:
    listener.join()

import pyautogui
import time

size = pyautogui.size()

isready = False
ingame = False

size_multiplier = size[0] / 2560, size[1] / 1440

print(f"{size[0]}, {size[1]} px  multiplier={size_multiplier[0]}, {size_multiplier[1]}")


def multi(x, y):
    global size_multiplier
    xy = x * size_multiplier[0], y * size_multiplier[1]
    xy = round(xy[0]), round(xy[1])
    return xy


def line_angle():
    print("")


rdy_btn_pos = multi(2400, 1080)
rdy_btn_col = 248, 255, 34

rdy_btn_die_pos = multi(2300, 900)
rdy_btn_die_col = 0, 119, 255

bus_icn_pos = multi(2185, 450)
bus_icn_col = 112, 167, 66

time.sleep(2)

while True:        
    if not isready:
        if pyautogui.pixelMatchesColor(rdy_btn_pos[0], rdy_btn_pos[1], rdy_btn_col, tolerance=32):
            pyautogui.click(rdy_btn_pos[0], rdy_btn_pos[1], interval=0.2)
            print("ready'ed up")
            isready = True
            ingame = False
        elif pyautogui.pixelMatchesColor(rdy_btn_die_pos[0], rdy_btn_die_pos[1], rdy_btn_die_col, tolerance=32):
            pyautogui.click(rdy_btn_die_pos[0], rdy_btn_die_pos[1], interval=0.2)
            print("ready'ed up")
            isready = True
            ingame = False
        else:
            print("waiting for ready button...")
            time.sleep(1)

    if isready:
        if pyautogui.pixelMatchesColor(bus_icn_pos[0], bus_icn_pos[1], bus_icn_col, tolerance=32):
            print("on bus waiting 15 seconds...")
            time.sleep(15)
            pyautogui.press('space')
            time.sleep(3)
            pyautogui.press('space', interval=0.2)
            ingame = True
            isready = False
        else:
            print("waiting for bus...")
            time.sleep(1)


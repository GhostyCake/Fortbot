import pyautogui
import time
import random

x = 0

print("Fortnite bot made by:")
print("Kake Mannen (aka Ghosty Cake)")
print("")
print("")
print(logo.read())
print("")
print("")



readybtn = 1820, 940,
bustimer = 1650, 330,
quitbtn = 1880, 1040,
busiconcol = 101, 159, 55
readybtncol = 243, 229, 70
scantime = 0.5
spamlevel = 1
# level 1 just important messages, level 2 lobby ingame waiting for game, level 3 color values

readycolorcheck = 0,0,0
buscheck = 0,0,0
readyclick = 0
busjump = 0
gamecount = 1
tfready = 0
tfbusjump = 0
size = pyautogui.size()

time.sleep(7)

print("Screen size ",size)
print("")

def f_lobby():
    pyautogui.moveTo(readybtn)
    time.sleep(0.129702731)
    pyautogui.click()
    print("waiting for game")
    print("game: ",gamecount)
    if spamlevel > 2:
        for num in range(0, 6):
           print("waiting...")
           time.sleep(0.7)


def f_busjump():
    pyautogui.press('space')
    print("Jumped from bus")
    f_ingame()




def f_ingamecheck():
    pyautogui.screenshot()
    if pyautogui.pixelMatchesColor(100, 1040, (35, 45, 55), tolerance=55) is True:
        print("Quitting game...")
        pyautogui.moveTo(quitbtn)
        time.sleep(0.4369231)
        pyautogui.click()
        print("Left the game")
    else:
        f_ingame()


def f_ingame():
    print("ingame")
    for num in range(0, 5):
        if spamlevel > 1:
            print("Ingame. game number: ",gamecount)
        walktime = random.randrange(1, 10)
        randnum = random.randrange(1, 4)
        if randnum == 1:
            walkkey = "w"
        if randnum == 2:
            walkkey = "a"
        if randnum == 3:
            walkkey = "s"
        if randnum == 4:
            walkkey = "d"
        pyautogui.keyDown(walkkey)
        time.sleep(walktime)
        pyautogui.keyUp(walkkey)
    f_ingamecheck()


def f_getpixel():
    image = pyautogui.screenshot()
    if spamlevel > 2:
        readybtncheck = image.getpixel((readybtn))
        buscheck = image.getpixel((bustimer))
        print("bus ",buscheck)
        print("ready",readybtncheck)
    if pyautogui.pixelMatchesColor(1650, 330, (101, 159, 55 ), tolerance=20) is True:
        f_startjump()
    if pyautogui.pixelMatchesColor(1820, 940, (243, 229, 70), tolerance=50) is True:
        f_lobby()
    if spamlevel > 2:
        print("No color match found")
        time.sleep(scantime)



def f_startjump():
    print("Waiting to jump...")
    time.sleep(15)
    f_busjump()

while x == 0:
    time.sleep(1)
    f_getpixel()
    if tfready == 1:
        f_lobby()
        gamecount = gamecount + 1
        readyclick = 0

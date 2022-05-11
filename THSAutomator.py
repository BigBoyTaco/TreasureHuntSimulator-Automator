import time, os, random

try:
    from pynput.keyboard import Key, Controller
    from pynput.mouse import Controller as MouseController
    from pynput.mouse import Button
    from win32api import GetSystemMetrics
except:
    input('press enter to run setup ')
    os.system('pip install pyautogui')
    os.system('pip install win32api')
    input('press enter to exit ')
    exit()

#make controling the mosue and keyboard eaiser
keyboard = Controller()
mouse = MouseController()

#get th resolution of the monitor
resX = GetSystemMetrics(0)
resY = GetSystemMetrics(1)

#scale depending on the monitor resolution
SellX = 1920 / resX * 50
SellY = 1080 / resY * 835

def start():
    timeLeft = input('please enter the time remaining (in mins) until the digsite collapses: ')
    try:
        timeLeft = int(timeLeft)
    except:
        input('not valid int ')
        start()
    input("reset then press enter to start and tab back to roblox ")
    time.sleep(5)
    keyboard.press('1')
    main(timeLeft)

def main(timeLeft):
    print('running...')
    toDig()
    time.sleep(2)
    startMine(timeLeft)
    #sell()

def toDig():
    keyboard.press('s')
    keyboard.press(Key.space)
    time.sleep(1)
    keyboard.press('a')
    time.sleep(0.5)
    keyboard.release('a')
    time.sleep(random.uniform(2.5, 3.5))
    keyboard.release('s')
    keyboard.release(Key.space)

def startMine(timeLeft):
    #auto clicker
    timeLeft = timeLeft * 60
    for x in range(timeLeft):
        time.sleep(1)
        mouse.click(Button.left)
    #open menu to reset
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(2)
    keyboard.press('r')
    keyboard.release('r')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #restart
    main(1860) #31 mins

'''def sell():
    #mouse mouse to sell button
    mouse.position = (SellX, SellY)
    time.sleep(0.5)
    #click sell button
    mouse.click(Button.left)
    time.sleep(1)
    #open menu to reset
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(2)
    keyboard.press('r')
    keyboard.release('r')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)'''
start()
input()
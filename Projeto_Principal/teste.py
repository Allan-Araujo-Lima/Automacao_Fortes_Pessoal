import pyautogui
import time

for x in pyautogui.getAllWindows():
    print(x.title)
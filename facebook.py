import pyautogui

import time

time.sleep(5)

for i in range(1, 100000):
    if i < 10:
        time.sleep(1)
        pyautogui.typewrite(f"00000{i}")
        pyautogui.press("enter")
        pyautogui.click()
    elif i < 100 and i > 10:
        time.sleep(1)
        pyautogui.typewrite(f"00000{i}")
        pyautogui.press("enter")
        pyautogui.click("left")
    elif i > 100:
        time.sleep(1)
        pyautogui.typewrite(f"0000{i}")
        pyautogui.press("enter")
    elif i > 1000:
        time.sleep(1)
        pyautogui.typewrite(f"000{i}")
        pyautogui.press("enter")
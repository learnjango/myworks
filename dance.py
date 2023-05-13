import pyautogui
import time

pyautogui.press('win')
pyautogui.typewrite('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(592, 858, duration=0.5)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite('https://www.youtube.com/watch?v=2Od-X7FQT2Q')
pyautogui.press('enter')
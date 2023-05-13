import pyautogui
import time

spam = int(input('Количество сообшения: '))
a = 0
massage = open('script.txt', 'r')
time.sleep(5)
for line in massage:
    pyautogui.typewrite(line)
    pyautogui.press('enter')
    time.sleep(0.1)
    a += 1
    if a == spam:
        break


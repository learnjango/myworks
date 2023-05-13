import pyautogui
from time import sleep

# Для того чтобы сделать паузу после каждое дейтве
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Разрешения екрана
size = pyautogui.size()
print(size)

# Место курсора (x, y)
x = pyautogui.position()
print(x)

# Перемешения мыша, duration время перемешения мыша
pyautogui.moveTo(960, 540, duration=1)

# Нажате, clicks это количество кликов, interval это задержка после клика
pyautogui.click(clicks=100, interval=0.05)
pyautogui.doubleClick()
pyautogui.tripleClick()
pyautogui.rightClick()
pyautogui.scroll(500)
pyautogui.middleClick()

# Перемешения с зажатем

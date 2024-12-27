import pyautogui
import pyperclip
import time

print(pyautogui.position())
time.sleep(0.1)

pyautogui.moveTo(1359,174)  
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("울산 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)
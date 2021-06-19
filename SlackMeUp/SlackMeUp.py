import pyautogui

while True:
    pyautogui.moveTo(100, 150)
    pyautogui.moveRel(0, 10)
    pyautogui.dragTo(100, 150)
    pyautogui.dragRel(0, 10)
import pyautogui
import time

n = int(pyautogui.prompt("Enter a number:"))

print(n)

time.sleep(3)
for i in range(1, n + 1):
    # print("#" * i) # i er man joto hobe # Totobar print hobe
    # pyautogui.write("*" * i, interval=0.25)
    # pyautogui.press('enter')

    for j in range(i):
        pyautogui.click()
        pyautogui.write('*')
    pyautogui.press('enter')
# *
# **
# ***
# ****
# *****

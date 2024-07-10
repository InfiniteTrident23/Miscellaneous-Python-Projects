import time, pyautogui

a = int(input("How many times do you wanna spam? "))
b = input("What do you wanna spam? ")
time.sleep(10)
i=0
while i<=a:
    pyautogui.typewrite(b)
    pyautogui.press("enter")
    i+=1

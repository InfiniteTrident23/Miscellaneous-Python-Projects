# Fun code to annoy your friends!
# Requires pyautogui library installation.
# After entering the spam string, take your cursor to the desired location
# WARNING: The program will not move the cursor, please shift it within 10 secs of the entering string!"

import time, pyautogui

a = int(input("How many times do you wanna spam? "))
b = input("What do you wanna spam? ")
time.sleep(10)
i=0
while i<=a:
    pyautogui.typewrite(b)
    pyautogui.press("enter")
    i+=1

#WhatsApp Auto BOT
import pyautogui as auto
import time

message = "My name is Ujjwal Neupane"
time.sleep(5)
for x in range(1,100):
    auto.write (message)
    auto.press('enter')
    time.sleep(1)


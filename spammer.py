import pyautogui
import keyboard
import sys
print("|     ||||||    |||||||||    ||||||||||   |||||     |||||   |||||     |||||   ||||||||   ||||||||  ")
print("|   |||         |||    |||   |||    |||   ||| ||||||  |||   ||| ||||||  |||   |||        |||   ||| ")
print("|   |||         |||    |||   |||    |||   |||   |||   |||   |||   |||   |||   |||        |||   ||| ")
print("|     |||||     |||||||||    ||||||||||   |||         |||   |||         |||   ||||||||   |||||||   ")
print("|         |||   |||          |||    |||   |||         |||   |||         |||   |||        |||  |||  ")
print("|         |||   |||          |||    |||   |||         |||   |||         |||   |||        |||   ||| ")
print("|    ||||||     |||          |||    |||   |||         |||   |||         |||   ||||||||   |||   ||| ")


word = input("Enter the text that you want to spam:=> ")
def sendMessage():
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        if keyboard.is_pressed('esc'):
                sys.exit()   


while True:
        sendMessage()
sendMessage()
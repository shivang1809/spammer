from tkinter import  Label, Text, Button, Tk, Frame
import pyautogui
import keyboard
import sys
import time

win=Tk()
win.title("Spammer")
win.maxsize(width=1000,height=310)
win.minsize(width=500,height=210)
win.configure(background="light green")
def get_input():
    value=my_text_box.get("1.0","end-1c")
    print(value) 
    time.sleep(1)
    def sendMessage():
        pyautogui.typewrite(value)
        pyautogui.press("enter")
        if keyboard.is_pressed('esc'):
            sys.exit()
    
    while True:
            sendMessage()
    sendMessage()

def help_bar():
    help_text = Label(win, text="●IMPORTANT: Imidiatly start pressed button the spamming starts just minimise the window and place the cursor where you want to spam the chat.", bg="light green")
    help_text.pack()
    h1 = Label(win, text="●While running programme press escape or Esc key twice to stop the programme.", bg="light green")
    h1.pack()
    h2 = Label(win, text="●You cannot do multitasking while spamming so do not run anyother programme before stoping the spammer.", bg="light green")
    h2.pack()
    h3 = Label(win, text="●If you not follow above instructions then it may be that your app get stuck or running same programme multipal time so to stop in that situation ", bg="light green")
    h3.pack()
    h4 = Label(win, text="press Ecs key on your keyboard, your programme will stop.", bg="light green")
    h4.pack()
    help_btn.destroy()
    win.mainloop()

title_bar= Frame(win, bg="light blue")
title_bar.pack(expand=1, fill="x")

title_t= Label(title_bar,text="Spammer", bg="light blue")
title_t.pack()

my_text_box=Text(win, height=5, width=100)
my_text_box.pack()

start_spamming= Button(win, height=2, width=30, text="Start Spamming",command= lambda:
get_input() )
start_spamming.pack()

help_btn = Button(win, text= "Help and How to use Spammer", command= lambda:help_bar())
help_btn.pack()


win.mainloop()
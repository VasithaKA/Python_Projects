import time
import pyautogui
import tkinter as tk


def screenShot():
    # time.sleep(5)
    img = pyautogui.screenshot()
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenShot
)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()

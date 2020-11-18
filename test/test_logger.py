import tkinter as tk
from src.beHacked import logger
import threading

def start():
    threading.Thread(target=log.start).start()
def stop():
    threading.Thread(target=log.stop).start()


log=logger()
main_window=tk.Tk("keylogger test")
start_button=tk.Button(main_window,text="start",command=start)
stop_button = tk.Button(main_window, text="stop", command=stop)
start_button.pack()
stop_button.pack()
main_window.mainloop()

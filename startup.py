from win32gui import GetWindowText, GetForegroundWindow, SetWindowPos, GetWindowRect
import win32con
import os, time
import pyautogui as pg

open_apps = []

while True:
    current_window = GetForegroundWindow()
    if current_window not in open_apps:
        open_apps.append(current_window)
    else:
        break
    pg.hotkey('shift', 'alt', 'tab')

print(open_apps)
   
def set_window_top():
    hwnd = GetForegroundWindow()
    (left, top, right, bottom) = GetWindowRect(hwnd)
    SetWindowPos(hwnd, win32con.HWND_TOPMOST, left, top, (right - left)+250, bottom - top, 0) 

pg.hotkey('shift', 'alt', 'tab')
time.sleep(2)
set_window_top()
import win32gui

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hwnd, win32gui.GetWindowText(hwnd))

win32gui.EnumWindows(winEnumHandler, None)
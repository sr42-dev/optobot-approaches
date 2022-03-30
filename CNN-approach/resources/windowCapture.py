import numpy as np
import win32gui
import win32ui
import win32con

class windowCapture :

    w = 0
    h = 0
    hwnd = None

    # constructor
    def __init__(self, windowname = None) :

        self.w = 854 # set window width
        self.h = 480 # set window height

        if windowname is None :
            self.hwnd = win32gui.GetDesktopWindow()
        else :
            # window to be captured
            self.hwnd = win32gui.FindWindow(None, windowname)
            if not self.hwnd :
                raise Exception('Window not found : {}'.format(windowname))

    def getScreenshot(self) :

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3] # remove comment only if using cv2.matchTemplate()
        img = np.ascontiguousarray(img)

        return img

    @staticmethod
    def listWindowNames():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)

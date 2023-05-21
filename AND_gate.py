from tkinter import *
from functools import partial

win = Tk()

win.title("Test")
win.option_add("*Fonts", "맑은고딕 25")
#win.geometry("1280x800")

canv = Canvas(win, width = 1280, height = 800, background = 'white')
canv.pack(padx = 0, pady = 0)

canv.create_line(230, 330, 200, 330, 200, 300, 230, 300, fill = "black", width = 3)
canv.create_line(230, 300, 250, 315, 230, 330, fill = "black", width = 3, smooth = True)

canv.create_oval(196, 304, 204, 312, fill = 'black')
canv.create_oval(196, 318, 204, 326, fill = 'black')
win.mainloop()


#무시
'''
class Point:            #점의 위치
    px = float()
    py = float()

    def __init__(self, x, y):
        self.px = x
        self.py = y

    def setPoint(self, x, y):
        self.px = x
        self.py = y

class Line:             
    start_P = Point(0, 0)
    end_P = Point(0, 0)

    #def __init__(self)

class AND_gate:
    start_P = Point(0, 0)




#abc = Point()

#abc.px = 1

#abc.aaa()
'''

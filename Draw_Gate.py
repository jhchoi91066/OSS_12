from tkinter import *
from functools import partial

win = Tk()

win.title("Test")
win.option_add("*Fonts", "맑은고딕 25")
#win.geometry("1280x800")

canv = Canvas(win, width = 1280, height = 800, background = 'white')
canv.pack(padx = 0, pady = 0)


#AND gate ========================================================================================
A_x = 500
A_y = 300

canv.create_line(A_x + 30, A_y + 36, A_x, A_y + 36, A_x, A_y, A_x + 30, A_y, fill = "black", width = 3)
canv.create_line(A_x + 30.3, A_y, A_x + 57, A_y + 18, A_x + 30.3, A_y + 36, fill = "black", width = 3, smooth = True)


canv.create_oval(A_x - 4, A_y + 5, A_x + 4, A_y + 13, fill = 'black')
canv.create_oval(A_x - 4, A_y + 23, A_x + 4, A_y + 31, fill = 'black')
canv.create_oval(A_x + 39, A_y + 14, A_x + 47, A_y + 22, fill = 'black')

#===================================================================================================

#OR gate============================================================================================
O_x = 100
O_y = 100

canv.create_line(O_x, O_y,       O_x + 40, O_y + 2,     O_x + 50, O_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(O_x, O_y + 36,  O_x + 40, O_y + 34,    O_x + 50, O_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(O_x, O_y,       O_x + 10, O_y + 20,    O_x, O_y + 36, fill = "black", width = 3, smooth = True)


canv.create_oval(O_x, O_y + 5, O_x + 8, O_y + 13, fill = 'black')
canv.create_oval(O_x, O_y + 23, O_x + 8, O_y + 31, fill = 'black')
canv.create_oval(O_x + 44, O_y + 14, O_x + 52, O_y + 22, fill = 'black')

#===================================================================================================


#Ex_OR gate============================================================================================
EO_x = 200
EO_y = 200

canv.create_line(EO_x, EO_y,       EO_x + 40, EO_y + 2,     EO_x + 50, EO_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(EO_x, EO_y + 36,  EO_x + 40, EO_y + 34,    EO_x + 50, EO_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(EO_x, EO_y,       EO_x + 10, EO_y + 20,    EO_x, EO_y + 36, fill = "black", width = 3, smooth = True)

canv.create_line(EO_x - 8, EO_y,       EO_x + 2, EO_y + 20,    EO_x - 8, EO_y + 36, fill = "black", width = 2.5, smooth = True)



canv.create_oval(EO_x, EO_y + 5, EO_x + 8, EO_y + 13, fill = 'black')
canv.create_oval(EO_x, EO_y + 23, EO_x + 8, EO_y + 31, fill = 'black')
canv.create_oval(EO_x + 44, EO_y + 14, EO_x + 52, EO_y + 22, fill = 'black')

#===================================================================================================


#NOT gate============================================================================================

N_x = 600
N_y = 300

canv.create_line(N_x, N_y,       N_x, N_y + 34,     N_x + 30, N_y + 17, N_x, N_y, fill = "black", width = 3)

canv.create_oval(N_x + 30, N_y + 12, N_x + 40, N_y + 22, width = 2)

#======================================================================================================


#NOR gate============================================================================================

NO_x = 900
NO_y = 100

canv.create_line(NO_x, NO_y,       NO_x + 40, NO_y + 2,     NO_x + 50, NO_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(NO_x, NO_y + 36,  NO_x + 40, NO_y + 34,    NO_x + 50, NO_y + 18, fill = "black", width = 3, smooth = True)

canv.create_line(NO_x, NO_y,       NO_x + 10, NO_y + 20,    NO_x, NO_y + 36, fill = "black", width = 3, smooth = True)


canv.create_oval(NO_x, NO_y + 5, NO_x + 8, NO_y + 13, fill = 'black')
canv.create_oval(NO_x, NO_y + 23, NO_x + 8, NO_y + 31, fill = 'black')
canv.create_oval(NO_x + 58, NO_y + 14, NO_x + 64, NO_y + 22, fill = 'black')

canv.create_oval(NO_x + 50, NO_y + 13, NO_x + 60, NO_y + 23, width = 2)

#==========================================================================================================================


#NAND gate ========================================================================================
NA_x = 1000
NA_y = 600

canv.create_line(NA_x + 30, NA_y + 36, NA_x, NA_y + 36, NA_x, NA_y, NA_x + 30, NA_y, fill = "black", width = 3)
canv.create_line(NA_x + 30.3, NA_y, NA_x + 57, NA_y + 18, NA_x + 30.3, NA_y + 36, fill = "black", width = 3, smooth = True)


canv.create_oval(NA_x - 4, NA_y + 5, NA_x + 4, NA_y + 13, fill = 'black')
canv.create_oval(NA_x - 4, NA_y + 23, NA_x + 4, NA_y + 31, fill = 'black')
canv.create_oval(NA_x + 51, NA_y + 14, NA_x + 61, NA_y + 22, fill = 'black')

canv.create_oval(NA_x + 44, NA_y + 13, NA_x + 54, NA_y + 23, width = 2)

#===================================================================================================



win.mainloop()

# Start, End

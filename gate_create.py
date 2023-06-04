from tkinter import *

app = Tk()
width = 1280
height = 720
canvas = Canvas(app, width=width, height=height, bg="white")
canvas.pack(padx=10, pady=10)

# And Gate - 좌클릭
def callback_mouse(event):
    print(event.x, event.y)
    shapes = canvas.create_line(event.x + 30, event.y + 36, event.x, event.y + 36, event.x, event.y, event.x + 30, event.y, fill = "black", width = 3)
    shapes = canvas.create_line(event.x + 30.3, event.y, event.x + 57, event.y + 18, event.x + 30.3, event.y + 36, fill = "black", width = 3, smooth = True)

    shapes = canvas.create_oval(event.x - 4, event.y + 5, event.x + 4, event.y + 13, fill = 'black')
    shapes = canvas.create_oval(event.x - 4, event.y + 23, event.x + 4, event.y + 31, fill = 'black')
    shapes = canvas.create_oval(event.x + 39, event.y + 14, event.x + 47, event.y + 22, fill = 'black')

# OR gate - 우클릭
def OR_gate(event):
    print(event.x, event.y)
    shapes = canvas.create_line(event.x, event.y,       event.x + 40, event.y + 2,     event.x + 50, event.y + 18, fill = "black", width = 3, smooth = True)

    shapes = canvas.create_line(event.x, event.y + 36,  event.x + 40, event.y + 34,    event.x + 50, event.y + 18, fill = "black", width = 3, smooth = True)

    shapes = canvas.create_line(event.x, event.y,       event.x + 10, event.y + 20,    event.x, event.y + 36, fill = "black", width = 3, smooth = True)


    shapes = canvas.create_oval(event.x, event.y + 5, event.x + 8, event.y + 13, fill = 'black')
    shapes = canvas.create_oval(event.x, event.y + 23, event.x + 8, event.y + 31, fill = 'black')
    shapes = canvas.create_oval(event.x + 44, event.y + 14, event.x + 52, event.y + 22, fill = 'black')

app.bind("<Button-1>", AND_gate)
app.bind("<Button-3>", OR_gate)

app.title('moving_gate')
app.geometry("1280x720")

app.mainloop()

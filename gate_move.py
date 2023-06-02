from tkinter import *

app = Tk()
width = 1280
height = 720
canvas = Canvas(app, width=width, height=height, bg="white")
canvas.pack(padx=10, pady=10)

def callback_mouse(event):
    print(event.x, event.y)
    canvas.delete("all")
    shapes = canvas.create_polygon(event.x, event.y, event.x+15, event.y, event.x+15, event.y+15, event.x, event.y+15, fill="black")

app.bind("<Button-1>", callback_mouse)

app.title('moving_picture')
app.geometry("1280x720")

app.mainloop()
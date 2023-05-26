from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from PIL import Image, ImageTk



root = Tk()
root.title('Writing Board')
root.geometry('1050x570+150+50')
root.resizable(False, False)


current_x = 0
current_y = 0
color = 'black'


def new_canvas():
    canvas.delete('all')
    display_color()

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y
    

def add_line(work):
    global current_x, current_y
    
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color, capstyle='round', smooth=True)
    
    current_x, current_y = work.x, work.y


def show_color(new_color):
    global color
    color = new_color
    

def chose_color():
    global color
    new_color = colorchooser.askcolor()
    color = new_color[1]


### eraser ###
eraser = Image.open('assets/eraser.png')
eraser = eraser.resize((37, 35))
eraser = ImageTk.PhotoImage(image=eraser)
Button(root, bg='#f2f3f5', command=new_canvas, image=eraser, cursor='hand2').place(x=30, y=400)   

# canvas of the color
colors = Canvas(root, bg='#ffffff', width=37, height=310, bd=0)
colors.place(x=30, y=60)


Button(root, text='Custom', bg='white', command=chose_color).place(x=10, y=10)




def display_color():
    
    id = colors.create_rectangle((10, 10, 30, 30), fill='aqua')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('aqua'))
    
    id = colors.create_rectangle((10, 40, 30, 60), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
    
    id = colors.create_rectangle((10, 70, 30, 90), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10, 100, 30, 120), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
    
    id = colors.create_rectangle((10, 130, 30, 150), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10, 160, 30, 180), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    
    id = colors.create_rectangle((10, 190, 30, 210), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    
    id = colors.create_rectangle((10, 220, 30, 240), fill='brown')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown'))
    
    id = colors.create_rectangle((10, 250, 30, 270), fill='grey')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('grey'))
    
    id = colors.create_rectangle((10, 280, 30, 300), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
    

display_color()


############ canvas, where we can draw ###########
canvas = Canvas(root, width=930, height=500, bg='white', cursor='hand2')
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)


############ slider, for changing the width of pen ###########

current_value = DoubleVar()

def get_current_value():
    return current_value.get()


slider = Scale(root, from_=1, to=100, orient='horizontal', variable=current_value)
slider.place(x=30, y=530)


root.mainloop()

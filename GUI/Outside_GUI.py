try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *

root = Tk()


leftFrame = Frame(root, width=200, height=600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

down = Button(leftFrame,
              text="DOWN", fg="red",
              command=lambda: move_down)
down.pack(side=BOTTOM)

up = Button(leftFrame,
                    text="UP", fg="red",
                    command = lambda: move_up)
up.pack(side=BOTTOM)

one = Button(leftFrame,
                    text="1",
                    command= lambda: go_first)
one.pack(side=BOTTOM, pady=1)


two = Button(leftFrame,
                    text="2",
                    command= lambda: go_first)
two.pack(side=BOTTOM, pady=1)

three = Button(leftFrame,
                    text="3",
                    command= lambda: go_second)
three.pack(side=BOTTOM, pady=1)

four = Button(leftFrame,
                    text="4",
                    command= lambda: go_third)
four.pack(side=BOTTOM, pady=1)

five = Button(leftFrame,
                    text="5",
                    command= lambda: go_third)
five.pack(side=BOTTOM, pady=1)


rightFrame = Frame(root, width=200, height=600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)


floor = Label(rightFrame,
              text=' ',
              command=lambda: request_floor)
floor.pack(side=RIGHT)


X = Button(rightFrame,
                text="X",
                command= lambda: firefighter)
X.pack(side=TOP, pady=0)

floor1 = Button(rightFrame,
                    text="1",
                    command= lambda: go_first)
floor1.pack(side=BOTTOM, pady=1)

floor2 = Button(rightFrame,
                    text="2",
                    command= lambda: go_second)
floor2.pack(side=BOTTOM, pady=1)

floor3 = Button(rightFrame,
                    text="3",
                    command= lambda: go_third)
floor3.pack(side=BOTTOM, pady=1)

floor4 = Button(rightFrame,
                    text="4",
                    command= lambda: go_fourth)
floor4.pack(side=BOTTOM, pady=1)

floor5 = Button(rightFrame,
                    text="5",
                    command= lambda: go_fifth)
floor5.pack(side=BOTTOM, pady=1)

open = Button(rightFrame,
                text="OPEN",
                command= lambda: open_door)
open.pack(side=BOTTOM, pady=10)

close = Button(rightFrame,
                    text="CLOSE",
                    command= lambda: close_door)
close.pack(side=BOTTOM, pady=1)

emergency = Button(rightFrame,
                    text="Emergency", fg="red", bg="white",
                    command= lambda: change_color(emergency))
emergency.pack(side=BOTTOM, pady=10)

firefighter = Label(rightFrame, text='Firefighter Operation')
firefighter.pack(side=TOP)



def request_floor():
    floor_num = current_floor()
    floor.config(text = floor_num)
    floor.after(100, request_floor)

def current_floor():
    ()



def change_color(emergency):
      current_color = emergency.cget("background")
      next_color = "white" if current_color == "red" else "red"
      emergency.config(background=next_color)
      root.after(1000, change_color)

def go_first():
      ()

def go_second():
      ()

def go_third():
      ()

def go_fourth():
      ()

def go_fifth():
      ()

def open_door():
      ()

def close_door():
      ()

def request_floor():
      ()

def firefighter():
      ()


def move_up():
      ()
      # call move_up function

def move_down():
      ()
      # call move_down function



root.mainloop()
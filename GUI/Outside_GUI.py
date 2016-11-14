from Elevator_System import ElevatorSystem

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *

root = Tk()

class Outside_GUI:
  def __init__(self, master):
    self.sys = ElevatorSystem()
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="UP", fg="red",
                         command=self.move_up)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="DOWN", fg="red",
                         command=self.move_down)
    self.slogan.pack(side=LEFT)

  def move_up(self):
      self.sys.add_request("move", 5, "passenger")

  def move_down(self):
      self.sys.add_request("move", 1, "passenger")
      # call move_down function
  def set_sys(self, system):
      self.sys = system


app = Outside_GUI(root)
root.mainloop()
from Elevator_System import ElevatorSystem

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *

class Inside_GUI:
  def __init__(self, master):
    self.sys = ElevatorSystem()
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="1",
                         command=self.go_first)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="2",
                         command=self.go_second)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="3",
                         command=self.go_third)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="4",
                         command=self.go_fourth)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="5",
                         command=self.go_fifth)
    self.slogan.pack()

    self.slogan = Button(frame,
                         text="OPEN",
                         command=self.open_door)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="CLOSE",
                         command=self.close_door)
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="Emergency", fg="red", bg="white",
                         command=self.change_color)
    #Test Button
    self.slogan.pack()
    self.slogan = Button(frame,
                         text="Do Request",
                         command=self.do_request)
    self.slogan.pack(side=LEFT)

  def change_color(self):
      current_color = self.slogan.cget("background")
      next_color = "green" if current_color == "red" else "red"
      self.slogan.config(background=next_color)
      root.after(1000, self.change_color)

  def go_first(self):
      self.sys.add_request("move", 1, "passenger")
  def go_second(self):
      self.sys.add_request("move", 2, "passenger")
  def go_third(self):
      self.sys.add_request("move", 3, "passenger")
  def go_fourth(self):
      self.sys.add_request("move", 4, "passenger")
  def go_fifth(self):
      self.sys.add_request("move", 5, "passenger")
  def open_door(self):
      self.sys.open_door()
  def close_door(self):
      self.sys.close_door()
  def do_request(self):
      self.sys.do_request()

  def set_system(self, system):
      self.sys = system



root = Tk()
app = Inside_GUI(root)
root.mainloop()
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *

class Inside_GUI:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="1",
                         command=self.go_first)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="2",
                         command=self.go_second)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="3",
                         command=self.go_third)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="4",
                         command=self.go_fourth)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="5",
                         command=self.go_fifth)
    self.slogan.pack(side=LEFT)

  def go_first(self):
      ()
  def go_second(self):
      ()
  def go_third(self):
      ()
  def go_fourth(self):
      ()
  def go_fifth(self):
      ()



root = Tk()
app = Inside_GUI(root)
root.mainloop()
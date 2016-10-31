try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *
    
class Outside_GUI:
  def __init__(self, master):
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
      ()
      # call move_up function

  def move_down(self):
      ()
      # call move_down function

root = Tk()
app = Outside_GUI(root)
root.mainloop()
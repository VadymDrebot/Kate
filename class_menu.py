from tkinter import *
class main:
  def __init__(self,title,geometry):
    self.master = root
    self.master.title=title
    self.master.geometry=geometry
    self.master.mainloop()

root = Tk()

window = Tk()
window.title("Работа с базами данных")   # заголовок окна
window.geometry("800x400+300+200")
btn = Button(window, text=" OK ").place(x=10, y=10)

window.mainloop()

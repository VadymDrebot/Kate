from tkinter import *
Window = Tk()
class Win:
    def __init__(self, Window, title, geometry):
        self.Window = Window
        self.Window.title(title)
        self.Window.geometry(geometry)

    def add_label(self,message):
        self.label=Label(self.Window, text=message)
    def add_button(self,but_text):
        Button(self.Window,text=but_text,command=self.com).pack()
    def add_entry(self):
        Entry(self.Window, width=30).pack()

    def run(self):
        self.label.pack()
        self.Window.mainloop()

    def com(self):
        self.label.configure(text="new")

    def create_child(self,title, geometry):
        ChildWindow(self.Window,title, geometry)

class ChildWindow:
    def __init__(self,Window, title, geometry):
        self.Window = Toplevel(Window)
        self.Window.title(title)
        self.Window.geometry(geometry)

    def add_but(self,but_text):
        Button(self.Window,text=but_text).pack()

def main():
    window1=Win(Window,"aaaa",'500x500+300+200')
    l1 = window1.add_label("label")
    b1=window1.add_button("buTTon11")
#    window1.create_child("dochernee",'300x300+700+200')
    w2=ChildWindow(Window,"dochernee","300x300+700+200")
    w2.add_but("chid_but")

    window1.run()



main()

from tkinter import *
root = Tk()
class Window:
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

    def add_label(self,message):
        self.label=Label(self.root, text=message)
    def add_button(self,but_text):
        Button(self.root,text=but_text,command=self.com).pack()
    def add_entry(self):
        Entry(self.root, width=30).pack()

    def run(self):
        self.label.pack()
        self.root.mainloop()

    def com(self):
        self.label.configure(text="new")

    def create_child(self,title, geometry):
        ChildWindow(self.root,title, geometry)

class ChildWindow:
    def __init__(self,parent, title, geometry):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.focus_set()
def main():
    window1=Window(root,"aaaa",'500x500+300+200')
    l1 = window1.add_label("label")
    b1=window1.add_button("buTTon11")
    window1.create_child("dochernee",'300x300+700+200')
    window1.run()



main()

from tkinter import *

window = Tk()
window.title("Работа с базами данных")   # заголовок окна
window.geometry("500x400+300+200")
mainmenu = Menu(window)
new_menu = Menu()
mainmenu.add_cascade(label="NEW", menu=new_menu)
new_menu.add_command(label="New SUPPLIERS")
new_menu.add_command(label="New SUPPLY_GROUP")

mainmenu.add_cascade(label="EDIT")
file_menu.add_command(label="Add item")
file_menu.add_command(label="Change item")
file_menu.add_command(label="Delete item")


window.config(menu=mainmenu)
window.mainloop()
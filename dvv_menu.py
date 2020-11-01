from tkinter import *
from tkinter.ttk import Radiobutton
import sqlite3
con = sqlite3.connect("suppliers.db")
add = []

def create_suppliers():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS suppliers""")
    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                    id TEXT PRIMARY KEY,surname TEXT,name TEXT,group_id INTEGER) """)
    users = [(12, 'ivanov', 'ivan', 48), (23, 'petrov', 'petr', 65), (45, 'sidorov', 'sidr', 48)]
    cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""", users)
    con.commit()
    return

def create_supply_group():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS supply_group""")
    cur.execute("""CREATE TABLE IF NOT EXISTS supply_group(
                        group_id INTEGER PRIMARY KEY,group_name)""")
    groups = [(48, 'global'), (65, 'local')]
    cur.executemany("""INSERT INTO supply_group VALUES(?,?)""", groups)
    con.commit()
    return

def out_suplliers():
    cur = con.cursor()
    cur.execute("""SELECT id,name,surname,group_id FROM suppliers """)
    a = 200
    for i in cur:
        lbl_create = Label(window, text=i,font="Arial 14")
        lbl_create.place(x=150, y=a)
        a += 40
    return

def out_supply_group():
    cur = con.cursor()
    cur.execute("""SELECT group_id,group_name FROM supply_group """)
    for a in range(200,550,10):
        lbl_create = Label(window, text="                          "
                                        "                           ")
        lbl_create.place(x=150, y=a)
    a = 200
    for i in cur:
        lbl_create = Label(window, text=i,font="Arial 14")
        lbl_create.place(x=150, y=a)
        a += 40
 #   con.commit()
    return

def add_item():
    window_add = Tk()
    window_add.title("Добавление элемента в таблицу")  # заголовок окна
    window_add.geometry("300x200+700+200")
    input_lbl = Label(window_add, text="  ID :   ")  # неактивна надпись слева
    input_lbl.place(x=20, y=10)
    input_lbl = Label(window_add, text="name:    ")  # неактивна надпись слева
    input_lbl.place(x=20, y=40)
    input_lbl = Label(window_add, text="surname: ")  # неактивна надпись слева
    input_lbl.place(x=20, y=70)
    input_lbl = Label(window_add, text="id_group: ")  # неактивна надпись слева
    input_lbl.place(x=20, y=110)

    message1= StringVar()
    message2= StringVar()
    message3= StringVar()
    message4 = StringVar()
    txt1 = Entry(window_add,textvariable=message1)  # ввод с клавиатуры
    txt1.place(x=120, y=10)
    txt2 = Entry(window_add, textvariable=message2)  # ввод с клавиатуры
    txt2.place(x=120, y=40)
    txt3 = Entry(window_add, textvariable=message3)  # ввод с клавиатуры
    txt3.place(x=120, y=70)
    txt4 = Entry(window_add, textvariable=message4)  # ввод с клавиатуры
    txt4.place(x=120, y=100)

    txt1.focus()  # фокус на окно ввода при запуске
  #  message.get()  # message= значение из окна ввода
    btn = Button(window_add,width=10,text="  OK  ",command=adding)  # конструктор BUTTON
    btn.place(x=70, y=140)
    btn = Button(window_add, width=10, text=" Отмена  ")  # конструктор BUTTON
    btn.place(x=160, y=140)
    window_add.mainloop()
    add.append(message1.get())
    add.append(message2.get())
    add.append(message3.get())
    add.append(message4.get())





    return
def adding():

    cur = con.cursor()
    cur.execute("""INSERT INTO suppliers (id,surname,name,group_id) VALUES (?,?,?,?)""", add)
    con.commit()
    return


add = []
window = Tk()
window.title("Работа с базами данных")   # заголовок окна
window.geometry("500x400+300+200")
mainmenu = Menu(window)
new_menu = Menu()
edit_menu= Menu()
view_menu= Menu()
mainmenu.add_cascade(label="   NEW   ", menu=new_menu)
new_menu.add_command(label="New SUPPLIERS",command=create_suppliers)
new_menu.add_command(label="New SUPPLY_GROUP",command=create_supply_group)

mainmenu.add_cascade(label="   EDIT   ",menu=edit_menu)
edit_menu.add_command(label="Add string",command=add_item)
edit_menu.add_command(label="Change string")
edit_menu.add_command(label="Delete string")

mainmenu.add_cascade(label="   VIEW   ",menu=view_menu)
view_menu.add_command(label="View SUPPLIERS",command=out_suplliers)
view_menu.add_command(label="View SUPPLY_GROUP",command=out_supply_group)
view_menu.add_separator()
view_menu.add_command(label="Search in SUPPLIERS")
view_menu.add_command(label="Search in SUPPLY_GROUP")
window.config(menu=mainmenu)



















window.mainloop()
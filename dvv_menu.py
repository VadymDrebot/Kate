from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
con = sqlite3.connect("students.db")
m_window = Tk()
add=[]                                   # пустой список для добавления элементов


def clean_window():                      # очистка экрана
    for i in range(10,900,5):
        l=Label(m_window, text="                                                                                         "
            "                                                                                                          ")
        l.place(x=20, y=i)
    return
########################################################
def create_tables():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS students""")
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                    st_id TEXT PRIMARY KEY,surname TEXT,name TEXT,fak_id TEXT,group_id TEXT,score TEXT) """)
    students_list = [('st_1', 'Иванов', 'Иван', 'fak_f','f_1','98'), ('st_2', 'Петров', 'Петр','fak_f','f_1','75'),
             ('st_3', 'Сидоров', 'Сеня','fak_e','e_1','93'),('st_4','Семенов','Ваня ','fak_e','e_1','65'),
             ('st_5','Васильков','Вася','fak_m','m_1','88'), ('st_6','Соколов','Федя','fak_m','m_1','78')]
    cur.executemany("""INSERT INTO students VALUES(?,?,?,?,?,?)""", students_list)
##########################
    cur.execute("""DROP TABLE IF EXISTS politeh""")
    cur.execute("""CREATE TABLE IF NOT EXISTS politeh(
                            fak_id TEXT PRIMARY KEY,fak_name TEXT,dekan TEXT)""")
    fakultets_list = [('fak_f','ФАВТ','Козловский'), ('fak_e', 'Экономический','Петровский'),('fak_m','Машиностроительный','Семановский')]
    cur.executemany("""INSERT INTO politeh VALUES(?,?,?)""", fakultets_list)
#########################
    cur.execute("""DROP TABLE IF EXISTS groups""")
    cur.execute("""CREATE TABLE IF NOT EXISTS groups(
                                group_id TEXT PRIMARY KEY,spec_name TEXT,number_of_students TEXT)"""),
    group_list = [('f_1', 'Программирование','32'), ('f_2', 'Комп. сети', '30'),('f_3', 'Безопастность','31'),
              ('e_1', 'Бухгалтерия', '28'), ('e_2', 'Внешняя экономика', '32'),('e_3', 'Торговля', '30'),
                  ('m_1', 'Автомобилестроение', '27'), ('m_2', 'Сельхоз техника', '25')]
    cur.executemany("""INSERT INTO groups VALUES(?,?,?)""", group_list)
    con.commit()
    return

################################# ПРОСМОТР ТРЕХ ТАБЛИЦ

def view_students():     ############# просмотр всех студентов-----база STUDENTS
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT st_id,surname,name,fak_id ,group_id ,score FROM students """)
    head=["ID студента"," Фамилия ","    Имя    "," ID фак-та "," ID группы ","Средний бал"]
    b = 20
    for i in range(6):
        main_lbl = Label(m_window, text=head[i], font="Arial 12").place(x=b, y=50)
        b += 120
    a = 100
    for item in cur:
        b=20
        for i in range(6):
            main_lbl=Label(m_window, text=item[i],font="Arial 14").place(x=b, y=a)
            b+=120
        a += 30
    return

def view_politeh():#################    просмотр факультетов  --- база POLITEH
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT fak_id,fak_name,dekan FROM politeh """)
    Label(m_window,text="факультеты ПОЛИТЕХА",font="Arial 18").place(x=160, y=10)
    head = ["ID", "Факультет", " Декан  "]
    b = 20
    for i in range(3):
        Label(m_window, text=head[i], font="Arial 12").place(x=b, y=70)
        b += 240
    a = 150
    for item in cur:
        b = 20
        for i in range(3):
            Label(m_window, text=item[i], font="Arial 12").place(x=b, y=a)
            b += 240
        a += 30
    return

def view_groups():#################    просмотр групп--таблица GROUPS
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT group_id ,spec_name ,number_of_students FROM groups""")
    head = ["  ID группы  ", "Специальность", "Кол-во студентов"]
    b = 20
    for i in range(3):
        Label(m_window, text=head[i], font="Arial 12").place(x=b, y=50)
        b += 230
    a = 150
    for item in cur:
        b = 20
        for i in range(3):
            Label(m_window, text=item[i], font="Arial 12").place(x=b, y=a)
            b += 230
        a += 30
    return

###################################

def new_student():

    list_fak=[]
    list_groups=[]
    cur = con.cursor()
    add_window=Toplevel()                       # создание дополнительного(дочернего) окна
    add_window.title("Добавление нового студента")  # заголовок окна
    add_window.geometry("370x280+700+500")
    def otmena_click():                         # закрытие окна ADD STRING без сохранения данных
        add_window.after(3, lambda: add_window.destroy())
    def add_click():                            # кнопка в окне ADD STRING--"добавления новой строки"
        for i in range(4):
            add.append(message[i].get())
        add.append(combo_fak_id.get())          #  пятый элемент-- из COMBOBOX
        add.append(combo_group_id.get())         #  шестой элемент-- из COMBOBOX
        cur = con.cursor()
        cur.execute("""INSERT INTO students (st_id ,surname ,name ,score,fak_id,group_id) VALUES (?,?,?,?,?,?)""", add)
        con.commit()
        add_window.after(3, lambda: add_window.destroy())  # закрытие окна через 3 млсек

    line = ["Введите ID","Введите фамилию: ","Введите имя:","Средний бал","Выберите фак-т:","Выберите группу:"]
    a=10
    for i in range(6):
        x = line[i]
        Label(add_window, text=x).place(x=20, y=a)              # неактивна надпись слева
        a+=30
    message1 = StringVar()
    message2 = StringVar()
    message3 = StringVar()
    message4 = StringVar()
    message=[message1,message2,message3,message4]
    a = 10
    for i in range(4):
        Entry(add_window, textvariable=message[i],width=23).place(x=150, y=a)      # ввод с клавиатуры
        a+=30

    combo_fak_id = Combobox(add_window)
    combo_fak_id.place(x=150, y=132)
    combo_group_id = Combobox(add_window)
    combo_group_id.place(x=150, y=162)

    cur.execute("""SELECT fak_id FROM politeh """)
    for item in cur:
        list_fak.append(item)                        # список факультетов
    combo_fak_id['values'] = list_fak
    combo_fak_id.current(0)

    cur.execute("""SELECT group_id FROM groups """)
    for item in cur:
        list_groups.append(item)                      #  список групп
    combo_group_id['values'] = list_groups
    combo_group_id.current(0)

    Button(add_window, text="    OK    ", command=add_click).place(x=100, y=220) # конструктор BUTTON
    Button(add_window, text="Отмена", command=otmena_click).place(x=165, y=220)  # конструктор BUTTON

    add_window.mainloop()
    return

def change_student():
    list = []
    cur = con.cursor()
    change_window = Toplevel()                    # создание дополнительного(дочернего) окна
    change_window.title("Изменение инфо студента")  # заголовок окна
    change_window.geometry("500x250+700+500")

    def search():
        global combo_2                            # combo второго списка: выбор id\имени\фамилии
        cur = con.cursor()
        if combo.get() == "ID":
            cur.execute("""SELECT st_id  FROM students """)
        elif combo.get() == "Фамилии":
            cur.execute("""SELECT surname  FROM students """)
        elif combo.get() == "Имени":
            cur.execute("""SELECT name  FROM students """)
        for item in cur:
            list.append(item)                      # список id или имен или фамилий в зависимости от состояния combo
        Label(change_window, text="Выбор").place(x=10, y=60)
        Button(change_window, text="   OK   ", command=choose).place(x=280, y=55)
        combo_2 = Combobox(change_window)
        combo_2['values'] = list
        combo_2.place(x=90, y=60)
        combo_2.current(0)
        return

    def choose():
        b=120
        global item
        change_st=[combo_2.get()]          # значение второго Combobox
        if combo.get() == "ID":
            cur.execute("""SELECT * FROM students WHERE st_id=?""", change_st)
        elif combo.get() == "Фамилии":
            cur.execute("""SELECT * FROM students WHERE surname=?""", change_st)
        elif combo.get() == "Имени":
            cur.execute("""SELECT * FROM students WHERE name=?""", change_st)
        for item in cur:
            for i in range(3):        # вывод вертикально:id,имени и фамилии выбранного студента
                Label(change_window, text=item[i],font=14).place(x=10, y=b)
                b+=45
        Button(change_window, text="Изменить", command=change_id).place(x=90, y=120)
        Button(change_window, text="Изменить", command=change_surname).place(x=90, y=160)
        Button(change_window, text="Изменить", command=change_name).place(x=90, y=200)
    def change_id():
        global new_id
        new_id = StringVar()
        Entry(change_window, textvariable=new_id,).place(x=180, y=125)
        Button(change_window, text=" Принять ", command=admit_id).place(x=360, y=120)
    def admit_id():                                # реакция на кнопку "ПРИНЯТЬ"
        list=[new_id.get(),item[0]]                # новое и старое ID
        cur.execute("""UPDATE students SET st_id=? WHERE st_id=? """,list)
        con.commit()
 ##########
    def change_surname():
        global new_surname
        new_surname = StringVar()
        Entry(change_window, textvariable=new_surname,).place(x=180, y=165)
        Button(change_window, text=" Принять ", command=admit_surname).place(x=360, y=160)

    def admit_surname():
        list=[new_surname.get(),item[1]]              # новое и старое фамилия
        cur.execute("""UPDATE students SET surname=? WHERE surname=? """,list)
        con.commit()
    def change_name():
        global new_name
        new_name = StringVar()
        Entry(change_window, textvariable=new_name,).place(x=180, y=205)
        Button(change_window, text=" Принять ", command=admit_name).place(x=360, y=200)
    def admit_name():
        list=[new_name.get(),item[2]]                   # новое и старое имя
        cur.execute("""UPDATE students SET name=? WHERE name=? """,list)
        con.commit()

    Label(change_window, text="Найти по").place(x=10, y=20)
    combo = Combobox(change_window)
    combo['values'] = ("ID", "Фамилии", "Имени")             # ищем по id\имени\фамилии
    combo.current(0)                                         # установка варианта( по умолчанию
    combo.place(x=90, y=20)
    btn = Button(change_window, text="   OK   ", command=search).place(x=280, y=15)

    change_window.mainloop()
    return


def delete_student():

    cur = con.cursor()
    del_window = Toplevel()             # создание дополнительного(дочернего) окна
    del_window.title("Удаление студента")  # заголовок окна
    del_window.geometry("400x250+700+500")
    def otmena_click():               # закрытие окна DELETE STUDENT без сохранения данных
        del_window.after(3, lambda: del_window.destroy())

    def delete():                     # удаление элемента,найденного в SEARCH()
        del_st=[combo_2.get()]          # значение второго Combobox
        if combo.get() == "ID":
            cur.execute("""DELETE FROM students WHERE st_id=?""", del_st)
        elif combo.get() == "Фамилии":
            cur.execute("""DELETE FROM students WHERE surname=?""", del_st)
        elif combo.get() == "Имени":
            cur.execute("""DELETE FROM students WHERE name=?""", del_st)
        con.commit()
        del_window.after(3, lambda: del_window.destroy())

    def search():
        global combo_2
        cur = con.cursor()
        list = []
        if combo.get() == "ID":
            cur.execute("""SELECT st_id  FROM students """)
        elif combo.get() == "Фамилии":
            cur.execute("""SELECT surname  FROM students """)
        elif combo.get() == "Имени":
            cur.execute("""SELECT name  FROM students """)

        for item in cur:
            list.append(item)
        combo_2 = Combobox(del_window)
        combo_2['values'] = list
        combo_2.place(x=120, y=70)
        combo_2.current(0)
        return

    combo = Combobox(del_window)
    combo['values'] = ("ID", "Фамилии", "Имени")
    combo.current(0)                                 # установка варианта по умолчанию
    combo.place(x=120, y=20)

    Button(del_window, text="Найти по", command=search).place(x=30, y=20)
    Button(del_window, text="Удалить студента", command=delete).place(x=30, y=120)
    Button(del_window, text="Отмена", command=otmena_click).place(x=170, y=120)

    del_window.mainloop()
    return




def find_student():
    add_window = Toplevel()   # создание дополнительного(дочернего) окна
    add_window.title("Поиск студента")  # заголовок окна
    add_window.geometry("400x250+700+500")
    def otmena_click():       # закрытие окна ADD STRING без сохранения данных
        add_window.after(3, lambda: add_window.destroy())

    def find_click():
        condition=combo.get()
        search = [find_mes.get(),]
        cur = con.cursor()
        if condition=="ID":
            cur.execute("""SELECT st_id ,surname ,name ,telefon FROM students WHERE st_id=?""",search)
        elif condition=="Фамилии":
            cur.execute("""SELECT st_id ,surname ,name ,telefon FROM students WHERE surname=?""", search)
        elif condition =="Имени":
            cur.execute("""SELECT st_id ,surname ,name ,telefon FROM students WHERE name=?""", search)
        elif condition == "Номеру тел.":
            cur.execute("""SELECT st_id ,surname ,name ,telefon FROM students WHERE telefon=?""", search)
        count = 0
        for el in cur:
            for i in range(4):
                Label(add_window, text=el,font="Arial 14").place(x=30, y=170)
                count = 1
        if count == 0:
            Label(add_window, text="Такого студента нет в базе",font="Arial 14").place(x=20, y=170)

    Label(add_window, text="Поиск по:").place(x=20, y=20)
    combo = Combobox(add_window)
    combo['values'] = ("ID","Фамилии","Имени" ,"Номеру тел.")
    combo.current(0)                                           # установите вариант по умолчанию
    combo.place(x=100,y=20)

    Button(add_window, text="    OK    ", command=find_click).place(x=70, y=120)
    Button(add_window, text="Отмена", command=otmena_click).place(x=140, y=120)

    find_mes = StringVar()
    Entry(add_window, textvariable=find_mes,width=33).place(x=20, y=60)  # ввод с клавиатуры
    add_window.mainloop()
    return

def main_window():
    global main_lbl
    m_window.title("Работа с базами данных")   # заголовок окна
    m_window.geometry("800x400+300+200")
    mainmenu = Menu(m_window)
    new_menu = Menu()
    edit_menu= Menu()
    view_menu= Menu()
    mainmenu.add_cascade(label="   FILE   ", menu=new_menu)
    new_menu.add_command(label="Новая база студентов", command=create_tables)
    new_menu.add_command(label="Загрузить базу студентов")#, command=create_students)
    new_menu.add_separator()
    new_menu.add_command(label="Новый студент",command=new_student)

    mainmenu.add_cascade(label="   EDIT   ",menu=edit_menu)
    edit_menu.add_command(label="Изменить инфо студента",command=change_student)
    edit_menu.add_command(label="Изменить инфо факультете")
    edit_menu.add_separator()
    edit_menu.add_command(label="Удалить студента",command=delete_student)

    mainmenu.add_cascade(label="   VIEW   ",menu=view_menu)
    view_menu.add_command(label="Просмотреть всех студентов  ",command=view_students)
    view_menu.add_command(label="Просмотреть факультеты", command=view_politeh)
    view_menu.add_command(label="Просмотреть группы", command=view_groups)
    view_menu.add_separator()
    view_menu.add_command(label="Найти студента",command=find_student)
    m_window.config(menu=mainmenu)
    m_window.mainloop()
    return

main_window()
con.close()

#   main_lbl.place_forget()
# window.after(3000, lambda: window.destroy())  # закрытие окна--3 сек





















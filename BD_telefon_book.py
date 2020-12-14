import sqlite3


#con=sqlite3.connect('database_worker_salary_post.db')
#cur=con.cursor()

def create_connection():
    try:
        conect = sqlite3.connect('mydatabase.db')
        return conect
    except Error:
        print(Error)


def create_database(conect):
    cur=conect.cursor()

    cur.execute("""DROP TABLE IF EXISTS tel_book""")

    cur.execute("""CREATE TABLE IF NOT EXISTS  tel_book (
    id_person INTEGER PRIMARY KEY AUTOINCREMENT,
    name_person TEXT    NOT NULL,
    sur_name TEXT    NOT NULL,
	tel_val INTEREG,
	coment CHAR(50)	
    );""")
    conect.commit()

def fill_data(conect):
    cur=conect.cursor()

    cur.execute("""INSERT INTO tel_book (name_person, sur_name, tel_val, coment)
        VALUES
	        ('Petya','Petrov',0674120141,'zxzxx'),
	        ('Vasya','Vaskin',0918084162,'qwe'),
	        ('Ivan','Ivanov',0935555555,'z'),
	        ('Masha','Manina',0677820141,'df'),
	        ('Sasha','Momin',0677970141,'qwe')  ;""")

    conect.commit()

def print_data(conect):
    cur = conect.cursor()

    print("┌───────────┬───────────┬───────────┬───────────────┬───────────┐")
    print("│id         │name       │surname    │tel            │coment     │")

    for row in cur.execute("""SELECT * FROM tel_book;"""):
        print("├───────────┼───────────┼───────────┼───────────────┼───────────┤")
        print("│", row[0], "\t\t│ ", row[1], "\t│ ", row[2], "\t│ ", row[3], "\t│", row[4], "\t\t│")
    print("└───────────┴───────────┴───────────┴───────────────┴───────────┘")


#        print(row)

def insert_data(conect):
    cur = conect.cursor()
    str_list = list()
    str = input("введите имя ")
    str_list.append(str)
    str = input("введите фамилию ")
    str_list.append(str)
    str = input("введите телефон ")
    str_list.append(str)
    str = input("введите коментарий ")
    str_list.append(str)

    cur.execute("""INSERT INTO tel_book (name_person, sur_name, tel_val, coment) VALUES(?,?,?,?) ;""", (str_list))
    conect.commit()

   # for row in cur.execute("""SELECT * FROM tel_book;"""):
   #     print(row)

def find_element(conect):
    cur=conect.cursor()
    str = input("введите значение которое вы хотите найти ")
    cur.execute("""SELECT * FROM tel_book 
        WHERE id_person=? OR name_person=? OR sur_name=? OR tel_val=? OR coment=? ;""", (str, str, str, str, str))

    rows=cur.fetchall()
   # print(len(rows))
    if len(rows)==0:
        print("такого элемента нет")
    else:
        for row in rows:
            print(row)

def edit_data(conect):
    cur=conect.cursor()
    str_id = int(input("введите значение id строку которого вы хотите изменить "))

    cur.execute("""SELECT * FROM tel_book WHERE id_person=?;""", (str_id,))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("элемента с таким id нет")
    else:
        str_name = input("введите новое имя ")
        str_surname = input("введите новую фамилию ")
        str_tel = input("введите новый номер телефона ")
        str_coment = input("введите новый коментарий ")
        cur.execute("""UPDATE tel_book SET name_person=?, sur_name=?, tel_val=?, coment=? 
            WHERE id_person=? ;""", (str_name,str_surname,str_tel,str_coment,str_id))
        conect.commit()
       # for row in cur.execute("""SELECT * FROM tel_book ;"""):
       #     print(row)

def delete_data(conect):
    cur=conect.cursor()
    str_id = input("введите значение id строку которого вы хотите удалить ")

    cur.execute("""SELECT * FROM tel_book WHERE id_person=?;""", (str_id,))
    rows = cur.fetchall()

    if len(rows) == 0:
        print("элемента с таким id нет")
    else:
        cur.execute("""DELETE FROM tel_book WHERE id_person=?;""", (str_id,))
        conect.commit()
       # for row in cur.execute("""SELECT * FROM tel_book ;"""):
        #    print(row)





con=create_connection()
create_database(con)
fill_data(con)
#insert_data(con)
#print_data(con)


print("ДОБРО ППОЖАЛОВАТЬ В ТЕЛЕФОННУЮ КНИГУ\n")
select=''
while select!='6':
    print("\n1. вывести на экран БД\n2. добавить запись в таблицу\n3. найти запись\n4. редактировать запись")
    print("5. удалить запись\n6. выйти из программы\n")
    select=input("выберите пунк меню, который вы хотите выполнить\t ")

    if select=='1':
        print("вы выбрали пункт меню 1 вывод БД на экран")
        print_data(con)

    elif select=='2':
        print("вы выбрали пункт меню 2 добавление записи в таблицу")
        insert_data(con)
        print_data(con)

    elif select == '3':
        print("вы выбрали пункт меню 3 поиск записи ")
        find_element(con)

    elif select == '4':
        print("вы выбрали пункт меню 4 редактирование записи ")
        edit_data(con)
        print_data(con)

    elif select == '5':
        print("вы выбрали пункт меню 5 удаление записи")
        delete_data(con)
        print_data(con)

    elif select == '6':
        print("вы выбрали пункт меню 6. ВЫХОД ")
        con.close()
    else:
        print("такого пункта меню нет\n")

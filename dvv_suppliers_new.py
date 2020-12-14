import sqlite3

def searching(): ############## поиск  и вывод на экран работника по ID,name or surname
    search=input("input id,name or surname: ")
    cur.execute("""SELECT id,surname,name FROM suppliers """)
    count = 0
    for el in cur:
            if search==el[1]:
                print("this is: ", el[2],"with ID: ",el[0])
                count = 1
            elif search==el[2]:
                print("this is: ", el[1],"with ID: ",el[0])
                count = 1
    if count==0:
        print("we dont have such name")
    return

def search(): ############## поиск  и вывод на экран работника по ID,name or surname

    aa=input("input id,name or surname: ")
    bb=[aa,aa,aa]
    cur.execute("""SELECT surname,name FROM suppliers WHERE id=? OR name=? OR surname=?""",bb)
    for i in cur:
        print(i)

##############################################################

con=sqlite3.connect("../raznoe/suppliers.db")
cur = con.cursor()
#####
cur.execute("""PRAGMA foreign_keys = ON""")
cur.execute("""DROP TABLE IF EXISTS suppliers""")
cur.execute("""DROP TABLE IF EXISTS supply_group""")
#cur.execute(""".headers on""")
#cur.execute(""".mode column""")
#########################       SUPPLY_GROUP

########################       SUPPLIERS
cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY,surname TEXT,name TEXT,group_id INTEGER NOT NULL)""")
users=[(12,'ivanov','ivan',48),(23,'petrov','petr',65),(34,'sidorov','sidr',48)]
cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""",users)
########################        SUPPLY_INFO

#a=[78,'durov','dur',65]
#cur.execute("""INSERT INTO suppliers VALUES(?,?,?,?)""",a)


cur.execute("""SELECT id,name,surname,group_id FROM suppliers """)
for i in cur:
    print(i)
search()

 #   cur.execute("""SELECT group_name,id,name,surname FROM  supply_group LEFT JOIN suppliers
  #              ON suppliers.group_id=supply_group.group_id  ORDER BY group_name""")
   # for i in cur:
   #     print(i)
#print("")
#searching()
con.commit()
con.close()
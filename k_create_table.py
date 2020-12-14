import sqlite3

con=sqlite3.connect('database_worker_salary_post.db')
cur=con.cursor()

cur.execute("""DROP TABLE IF EXISTS test_datatypes""")
cur.execute("""DROP TABLE IF EXISTS test2_datatypes""")
cur.execute("""DROP TABLE IF EXISTS test3_datatypes""")

cur.execute("""CREATE TABLE IF NOT EXISTS  test_datatypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	val
    );""")



cur.execute("""INSERT INTO test_datatypes (val)
VALUES
	(1),
	(2),
	(10.1),
	(20.5),
	('A'),
	('B'),
	(NULL),
	(x'0010'),
	(x'0011');""")

cur.execute("""CREATE TABLE IF NOT EXISTS  test2_datatypes (
    val_id INTEGER PRIMARY KEY AUTOINCREMENT,
    value,
    num INTEGER NOT NULL DEFAULT 100
    );""")




cur.execute("""CREATE TABLE IF NOT EXISTS  test3_datatypes (
    id_person INTEGER PRIMARY KEY AUTOINCREMENT,
    name_person TEXT    NOT NULL,
    sur_name TEXT    NOT NULL,
	tel_val INTEREG,
	coment CHAR(50)	
    );""")



cur.execute("""INSERT INTO test3_datatypes (name_person, sur_name, tel_val, coment)
VALUES
	('Petya','Petrov',0674120141,'zxzxzx'),
	('Vasya','Vasechkin',0918084162,'wewewe'),
	('Ivan','Ivanov',0935555555,'z'),
	('Masha','Manina',0677820141,'df'),
	('Sasha','Momin',0677970141,'qwe')  ;""")

con.commit()
for row in cur.execute("""SELECT * FROM test3_datatypes;"""):
    print(row)

#ROREIGN KEY (for_key) REFERENCES test_datatypes (id)
#cur.execute("""INSERT INTO test2_datatypes SELECT id, val FROM test_datatypes ;""")
c=cur.execute("""SELECT * FROM test_datatypes  ;""")

new_data=list()
for row in c:
    new_data.append(row)
   # print(new_data)

#копируем 1-ую и 2-ую колонку первой таблицы во вторую таблицу у которой три колонки
cur.executemany("""INSERT INTO test2_datatypes VALUES(?,?,100) ;""",(new_data))

#добавляем строку в первую таблицу
str_list=list()
str=input("введите значение которое вы хотите добавить в первую таблицу ")
str_list.append(str)

cur.execute("""INSERT INTO test_datatypes (val) VALUES(?) ;""",(str,))
con.commit()

cur.execute("""SELECT * FROM test_datatypes;""")
print(cur.fetchall())

#найти элемент в таблице один
str_list=list()
str=input("введите значение которое вы хотите найти в третьей таблице ")
str_list.append(str)
cur.execute("""SELECT * FROM test3_datatypes 
    WHERE id_person=? OR name_person=? OR sur_name=? OR tel_val=? OR coment=? ;""",(str,str,str,str,str))
print(cur.fetchall())

#изменяем значение id введенного с клавиатуры
str_id=int(input("введите номер id значение которого вы хотите изменить в первой таблице "))
for row in cur.execute("""SELECT * FROM test_datatypes WHERE id=?;""", (str_id,) ):
  #  if str_list[0]==row[0]:
   str_val = input("введите новое значение ")
   cur.execute("""UPDATE test_datatypes SET val=? WHERE id=? ;""", (str_val,str_id))
   con.commit()
cur.execute("""SELECT * FROM test_datatypes ;""")
print(cur.fetchall())

cur.execute("""SELECT
	id,
	val,
	typeof(val)
FROM
	test_datatypes;""")

cur.execute("""SELECT
	val_id,
	value,
	num
FROM
	test2_datatypes;""")

for row in cur:
   # print(cur.fetchall())
    print(row)


con.close()
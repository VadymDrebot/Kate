import sqlite3

def column_name(con):
    # SHOW COLUMN
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM workers')
    r = cur.fetchone()
    print(r.keys())
    print("type(r)= ",type(r))
    print("tuple(r)= ",tuple(r))
    print("len(r)=",len(r))
    print("r[2]=",r[2])
    print("r['fname_worker']=",r['fname_worker'])
    return r.keys()

def show_table_name(cursor):
    # SHOW TABLES
    cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    print(cur.fetchall())

def show_sql_create(cursor):
    # SHOW SQL
    cursor.execute("""SELECT sql FROM sqlite_master WHERE name='workers';""")
    print(cursor.fetchall())

def find_element(cursor,tupl):

    print("что хотите найти: ")
    print(" \n1. по номеру в списке работника \n2. по фамилии работника\n3. по имени работника")
    print("4. по дате рождения работника \n5. по адресу работника")
    i=int(input("выберите соответствующий пункт: "))
    s=input("введите искомое значение ")
    i-=1
    print(tupl)
    print(tupl[i])
    print(int(s))
    cursor.execute("""SELECT * FROM workers WHERE ?=?""",(tupl[i],int(s)))

    #?=?""",(tupl[i],s))
    rows=cursor.fetchall()
    if len(rows)==0:
        print("такого элемента нет")
    else:
        for r in rows:
            print(r)

conect=sqlite3.connect('db_worker_salary_post.db')
cur=conect.cursor()

cur.execute("""DROP TABLE IF EXISTS workers""")

cur.execute("""CREATE TABLE IF NOT EXISTS workers(
    id_worker INTEGER PRIMARY KEY,
    fname_worker TEXT    NOT NULL,
    lname_worker  TEXT  NOT NULL,
	birth_worker TEXT,
	adres_worker TEXT)	
    """)

cur.execute("""INSERT INTO workers (id_worker, fname_worker, lname_worker, birth_worker, adres_worker)
        VALUES
	        (1,'Petrov','Petya','2.02,1980','filotova srt 24'),
	        (2,'Vaskin','Vasya','19.08.1970','jukova str 8'),
	        (3,'Ivanov','Ivan','4.04.1990','koroliava 98,apt 8'),
	        (4,'Manina','Masha','23.01.1984','levitana 7'),
	        (5,'Momin','Sasha','5.07.1987','lva tolstogo 10') 
	         ;""")

conect.commit()

cur.execute('SELECT * FROM workers')
r = cur.fetchall()
for x in r:
    print(x)

cur.execute("""DROP TABLE IF EXISTS worker_salary""")

cur.execute("""CREATE TABLE IF NOT EXISTS worker_salary(
    id_salary INTEGER PRIMARY KEY,
    salary INTEGER   NOT NULL,
    bonux INTEGER   NOT NULL,
	id_worker      INTEGER,
	FOREIGN KEY (id_worker)  REFERENCES workers (id_worker) 
       ON UPDATE CASCADE
       ON DELETE CASCADE)	
    ;""")

cur.execute("""INSERT INTO worker_salary (salary, bonux, id_worker)
        VALUES
	        (5000,50,2),
	        (650,20,1),
	        (10000,10,5)
	        ;""")

conect.commit()


cur.execute('SELECT * FROM worker_salary')
r = cur.fetchall()
for x in r:
    print(x)

cur.execute("""SELECT fname_worker, lname_worker, salary  FROM workers 
    INNER JOIN worker_salary USING (id_worker)  ORDER BY fname_worker""")
r = cur.fetchall()
for x in r:
    print(x)

cur.execute("""SELECT salary, fname_worker  FROM worker_salary 
    LEFT JOIN workers USING (id_worker) ORDER BY salary DESC """)
r = cur.fetchall()
for x in r:
    print(x)

t=column_name(conect)

find_element(cur,t)

#show table
#show_table_name(cur)

#show sql
#show_sql_create(cur)

#show colum_name
#column_name(conect)





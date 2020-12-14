import sqlite3

def inser_data():
    l=list()
    i_list=input("введите id ")
    l.append(i_list)
    i_list = input("введите name ")
    l.append(i_list)
    i_list = input("введите surname ")
    l.append(i_list)
    i_list = input("введите birth ")
    l.append(i_list)
    print(l)


con=sqlite3.connect('database_worker_salary_post.db')
cur=con.cursor()

cur.execute("""DROP TABLE IF EXISTS workers""")

cur.execute("""CREATE TABLE IF NOT EXISTS workers (
             workerid INTEREG PRIMARY KEY,
             name TEXT,
             surname TEXT,
             birth TEXT)""")


worker=[('001','Ivan ','Ivanov','19-09-1980'),('002','Petya','Petrov','19-06-1976'),('003','Vasya','Vasilev','19-09-1980')]
cur.executemany("""INSERT INTO workers (workerid,name,surname,birth) VALUES (?,?,?,?)""",worker)
con.commit()



n=('Vasya',)
cur.execute("""SELECT * FROM workers WHERE name=?""",n)
print(cur.fetchone())

#rows=cur.fetchall()
print("┌───────────┬───────────┬───────────┬────────────┐")
print("│id         │name       │surname    │birth       │")

for row in cur.execute("""SELECT * FROM workers """):
    print("├───────────┼───────────┼───────────┼────────────┤")
    print("│", row[0], "\t\t│", row[1], "\t│", row[2], "\t│", row[3], "│")
print("└───────────┴───────────┴───────────┴────────────┘")
    #print(row)
   # for i in row:
   #     print(i,"\t")

con.close()

inser_data()




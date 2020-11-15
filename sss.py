import sqlite3
import csv
a=[]

with open('bok.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i[0],i[1])
#print(row[0][6])


#!/usr/bin/python3
"""Module that uses 'MySQLdb' import to lists all 'states' in
'hbtn_0e_0_usa' database
"""
import MySQLdb

if __name__ != "__main__":
    exit()

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root",
                     db="hbtn_0e_0_usa", charset="utf8")

cur = db.cursor()
cur.execute("SELECT * FROM states FROM ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()

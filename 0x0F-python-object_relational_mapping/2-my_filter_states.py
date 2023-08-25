#!/usr/bin/python3
"""Module that uses 'MySQLdb' import to display all values in
the 'states' table of 'hbtn_0e_0_usa' database where 'name'
matches an argument passed
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{argv[4]}'")
    records = cur.fetchall()
    for record in records:
        print(record)
    cur.close()
    db.close()

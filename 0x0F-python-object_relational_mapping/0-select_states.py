#!/usr/bin/python3
<<<<<<< HEAD
"""Module that uses 'MySQLdb' import to lists all 'states'
in 'hbtn_0e_0_usa' database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` FROM ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

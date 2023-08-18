#!/usr/bin/python3
"""Module that uses 'MySQLdb' import to lists all 'states' in
'hbtn_0e_0_usa' database
"""
import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root",
                     db="hbtn_0e_0_usa", charset="utf8")
cur = db.cursor

cur.execute("SELECT states FROM hbtn_0e_0_usa ORDER BY id ASC")

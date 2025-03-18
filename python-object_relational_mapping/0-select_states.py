#!/usr/bin/python3

"""
This script connects to a database from mysql
"""

import MySQLdb
import os


"""
This script connects to a database from mysql
"""

username = 'root'
password = os.getenv('DB_PASSWORD')
database = 'hbtn_0e_0_usa'

db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.close()


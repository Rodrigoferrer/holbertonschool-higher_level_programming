#!/usr/bin/python3

"""
Script that lists --
from the database hbtn_0e_0_usa preventing slq injection by passing by parameters.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = ("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """)

    cursor.execute(query, ("{}%".format(state_name),))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

#!/usr/bin/python3

"""
Script that lists all states with a name
starting with a given letter 
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    input_from_user= sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
    SELECT id, name
    FROM states
    WHERE BINARY name LIKE %s
    ORDER BY id ASC;
    """

    cursor.execute(query, ("{}%".format(input_from_user),))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

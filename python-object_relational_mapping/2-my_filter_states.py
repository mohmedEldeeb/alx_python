#!/usr/bin/python3
"""
    My module Write a script that lists all
    states with a name starting
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    matches = sys.argv[4]
    host = "localhost"

    database = MySQLdb.connect(host=host, user=username, passwd=password, db=dbName)
    cur = database.cursor()
    query = "SELECT * from states WHERE name = BINARY '{}' ORDER BY id ASC"
    cur.execute(query.format(matches))

    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    database.close()
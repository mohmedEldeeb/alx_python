#!/usr/bin/python3
# This module lists all states in the database
# imports module MySQLdb
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    database = MySQLdb.connect(host='localhost', user=username,
                               passwd=password, db=dbName)

    cur = database.cursor()
    query = "SELECT * from states ORDER BY id ASC"
    cur.execute(query)

    # obtaining the results
    data = cur.fetchall()
    for row in data:
        print(row)

    # close cursor
    cur.close()

    # close database
    database.close()


if __name__ == "__main__":
    main()
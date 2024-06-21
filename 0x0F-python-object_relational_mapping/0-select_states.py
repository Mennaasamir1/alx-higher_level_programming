#!/usr/bin/python3
import  MySQLdb
import sys

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3386)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()

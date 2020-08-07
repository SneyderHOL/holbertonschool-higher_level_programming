#!/usr/bin/python3
"""Select states module"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    size = len(sys.argv) - 1
    db = None
    if size == 3:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        res = cur.execute("SELECT * FROM states ORDER BY id ASC")
        results = cur.fetchall()
        for result in results:
            print(result)
        cur.close()
        db.close()

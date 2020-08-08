#!/usr/bin/python3
"""Select cities module"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    size = len(sys.argv) - 1
    db = None
    if size == 3:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN "\
                "states AS s ON c.state_id = s.id ORDER BY c.id ASC"
        res = cur.execute(query)
        results = cur.fetchall()
        for result in results:
            print(result)
        cur.close()
        db.close()

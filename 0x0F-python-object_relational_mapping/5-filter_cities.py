#!/usr/bin/python3
"""Select cities module"""


def escape_chars(string):
    """ function to escape characers use in sql"""
    esc_array = ['\\x00', '\\n', '\\r', '\\', '\'', '"', '\\x1a', '%', '_']
    if type(string) is str:
        for element in esc_array:
            if element in string:
                string = string.replace(element, "\\" + element)
    return string

if __name__ == "__main__":
    import MySQLdb
    import sys
    size = len(sys.argv) - 1
    db = None
    if size == 4:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        var_input = escape_chars(sys.argv[4])
        query = "SELECT c.name FROM cities AS c INNER JOIN "\
                "states AS s ON c.state_id = s.id WHERE s.name LIKE 'Texas' "\
                "ORDER BY c.id ASC".format(var_input)
        res = cur.execute(query)
        results = cur.fetchall()
        val = ""
        for result in results:
            val += result[0] + ", "
        print(val[:-2])
        cur.close()
        db.close()

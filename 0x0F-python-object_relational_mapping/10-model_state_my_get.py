#!/usr/bin/python3
"""Select States module"""


def escape_chars(string):
    """ function to escape characers use in sql"""
    esc_array = ['\\x00', '\\n', '\\r', '\\', '\'', '"', '\\x1a', '%', '_']
    if type(string) is str:
        for element in esc_array:
            if element in string:
                string = string.replace(element, "\\" + element)
    return string

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    size = len(sys.argv) - 1
    engine = None
    if size == 4:
        conn_values = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
                    "".format(sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(conn_values, pool_recycle=3600)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        value = escape_chars(sys.argv[4])
        states_list = session.query(State).filter(State.name.like(value))\
                                          .first()
        if states_list is None:
            print("Not found")
        else:
            print(states_list.id)
        session.commit()
        session.close()

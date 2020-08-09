#!/usr/bin/python3
"""Script that lists all City objects from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size == 3:
        conn_values = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
                    "".format(sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(conn_values, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states_list = session.query(State, City)\
                             .filter(State.id == City.state_id)\
                             .order_by(City.id).all()
        if states_list is None:
            print("Not found")
        else:
            for s, c in states_list:
                print("{}: {}".format(c.id, c.name), end="")
                print(" -> {}".format(s.name))
        session.commit()
        session.close()

#!/usr/bin/python3
"""Script that list all State objects, and corresponding City objects in the
    database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, lazyload
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
        """states_list = session.query(State, City)\
                             .join(City)\
                             .order_by(State.id, City.id).all()"""
        states_list = session.query(State).order_by(State.id).all()
        if states_list is None:
            print("Not found")
        else:
            for state in states_list:
                print("{}: {}".format(state.id, state.name))
                for city in state.cities:
                    print("\t{}: {}".format(city.id, city.name))
        session.commit()
        session.close()

#!/usr/bin/python3
"""Script that creates the "State California" with the city "San Francisco"
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
        new_state = State()
        new_state.name = "California"
        session.add(new_state)
        session.flush()
        new_city = City()
        new_city.name = "San Francisco"
        new_city.state_id = new_state.id
        session.add(new_city)
        session.commit()
        session.close()

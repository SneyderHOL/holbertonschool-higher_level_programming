#!/usr/bin/python3
"""Select States module"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    size = len(sys.argv) - 1
    engine = None
    if size == 3:
        conn_values = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
                    "".format(sys.argv[1], sys.argv[2], sys.argv[3])
#        create an engine
        engine = create_engine(conn_values, pool_recycle=3600)
#        generate database shema
        Base.metadata.create_all(engine)
#        create a configured 'Session' class
        Session = sessionmaker(bind=engine)
#        create new session
        session = Session()
        state_element = session.query(State).filter(State.id == 2).first()
        state_element.name = "New Mexico"
        session.commit()
        session.close()

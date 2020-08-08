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
        engine = create_engine(conn_values, pool_recycle=3600)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_object = State()
        new_object.name = "Louisiana"
        session.add(new_object)
        session.commit()
        session.close()

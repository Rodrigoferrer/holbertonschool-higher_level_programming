#!/usr/bin/python3
"""Define the State class and create the states table in the database."""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Esta clase la creo para que todas hereden de ella
Base = declarative_base()

class State(Base):
    """State class that maps to the states table in the database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Verificar por cantidad de args
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # reo el motor
    engine = create_engine(f'mysql+mysqldb://{root}:{admin}@localhost/{hbtn_0e_6_usa}', pool_pre_ping=True)

   # Crear todo
    Base.metadata.create_all(engine)

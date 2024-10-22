from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://serhii.ravliuk:kabosina2517@localhost/students_db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)




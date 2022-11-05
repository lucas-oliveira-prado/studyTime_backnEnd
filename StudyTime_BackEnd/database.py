from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+mysqldb://root:@localhost:3306/study_time")
SessionLocal = sessionmaker(bind=engine) 

def get_db():     
    db = SessionLocal()     
    return db

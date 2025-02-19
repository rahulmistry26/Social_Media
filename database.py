from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base

DATABASE_URL = "Your Database URl"
engine = create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base =declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db =SessionLocal()
    try: 
        yield db
    except:
        db.close()
        
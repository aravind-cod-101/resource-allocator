from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL


class Database:
    def __init__(self,config):
        self.engine = create_engine(config)
        self.session = sessionmaker(bind=self.engine)

    def get_db(self):
        db = self.session()
        try: 
            yield db
        finally:
            db.close()
            
            
            
db_session = Database(DATABASE_URL)
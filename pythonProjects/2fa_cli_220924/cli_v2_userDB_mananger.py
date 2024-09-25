from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class users_list(Base):
    __tablename__ = "users"

    user_no=Column("user_no", Integer, primary_key=True)
    user_name=Column("user_names", String, nullable=False)
    user_keys_db=Column("user_keys_path", String, nullable=False)

    def __init__(self, user_no, user_names, user_keys_db):
        self.user_no = user_no
        self.user_names = user_names
        self.user_keys_db = user_keys_db

    #def _repr__(self):

engine = create_engine("sqlite:///users_list.db", echo=True) #connects the Database

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user=users_list(1, "Ameer", "KEys_exAmPle1")
session.add(user)
session.commit()
print(user)
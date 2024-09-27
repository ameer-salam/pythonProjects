import os
from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


def check_user_exists():
    return os.path.exists("C:/Users/salam/OneDrive/Documents/Projects/pythonProjects/pythonProjects/2fa_cli_220924/OpenAuth_v121_users_list.db")

#to define a base class
Base = declarative_base()

class User_list(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False)
    user_mail = Column(String(100), nullable=False, unique=True)
    user_key_db = Column(String(255), nullable=False)

    def __repr__(self):
        print(f"<User_list(id={self.id}, username = {self.user_name}, mail = {self.user_mail}, path = {self.user_key_db})>")
        #return f"<User_list(id={self.id}, username = {self.user_name}, mail = {self.user_mail}, path = {self.user_key_db})>"

    def add_new_user(user_name, user_mail):
        new_user = User_list(user_name=user_name, user_mail=user_mail, user_key_db="NOW DUMB")
        session.add(new_user)
        session.commit()
        print(f"New user {user_name} added!")


#insert a new user 
#new_user = User_list(user_name="ameer salam", user_mail="ameer@mail", user_key_db="wassup bro")
#session.add(new_user)
#session.commit

def printAll():
    users = session.query(User_list).all()
    for user in users:
        User_list.__repr__()


"""
if (os.path.exists("C:/Users/salam/OneDrive/Documents/Projects/pythonProjects/pythonProjects/2fa_cli_220924/OpenAuth_v121_users_list.db"))==False:
        print("Existing user")
        engine = create_engine('sqlite:///C:/Users/salam/OneDrive/Documents/Projects/pythonProjects/pythonProjects/2fa_cli_220924/OpenAuth_v121_users_list.db', echo=True)
        #create the table in the database
        Base.metadata.create_all(engine)

        #create a session to interract with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        return False
    else:
        #create the table in the database
        Base.metadata.create_all(engine)

        #create a session to interract with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        return True
"""
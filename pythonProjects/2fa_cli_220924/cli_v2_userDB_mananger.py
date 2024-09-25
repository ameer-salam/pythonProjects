from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class users_list(Base):
    __tablename__ = "users"

    user_no=Column("user_no", Integer, primary_key=True)
    user_name=Column("user_name", String, primary_key=False)
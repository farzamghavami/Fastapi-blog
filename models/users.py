from textwrap import indent
from database import Base
from sqlalchemy import Column,String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Integer, default=0)  # 1: admin, 0: normal user
    posts = relationship("Post", back_populates="owner")

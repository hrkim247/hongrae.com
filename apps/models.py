from sqlalchemy import Column, Integer, String
from apps.database import Base

class User(Base):

    __tablename__ = "user"
    
    num = Column(Integer, primary_key=True)
    id = Column(String, unique=True)
    pw = Column(String, unique=True)

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

    def __repr__(self):
        return "<{0}, {1}>".format(self.id, self.pw)

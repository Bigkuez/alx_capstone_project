from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base =declarative_base()

class Contact(Base):
    __tablename__ ="contactme"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55))
    email = Column(String(100))
    message = Column(String(255))
    def __init__(self, name, email, message):
        self.name = name 
        self.email = email
        self.message =  message

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from apiframework.models.db_connection import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    def __init__(self,id,name):
        self.id = id
        self.name = name
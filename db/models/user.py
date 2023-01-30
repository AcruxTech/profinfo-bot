from sqlalchemy import Column, BigInteger, Text

from db.base import Base


class User(Base):
    
    __tablename__ = 'users'
    
    id = Column(BigInteger(), primary_key=True)
    uuid = Column(BigInteger())             # telegram unique id: int
    status = Column(Text())

    
    def __repr__(self):
        return f'User({self.id}, {self.uuid}, {self.name}, {self.group_id})'

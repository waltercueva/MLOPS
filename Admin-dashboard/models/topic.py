from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, DateTime, Text, Float
from sqlalchemy.orm import relationship

from . import Base

class Topic(Base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    score = Column(Float(18, 9))
    law_id = Column(String(20), ForeignKey('law.id'))
    law = relationship("Law", back_populates="topic")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

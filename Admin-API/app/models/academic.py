from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from . import Base

class Academic(Base):
    __tablename__ = 'academic'
    id = Column(Integer, primary_key=True)
    place = Column(String(20))
    province = Column(String(20))
    status = Column(String(20))
    start_year = Column(Integer)
    end_year = Column(Integer)
    degree = Column(String(30))
    career = Column(String(30))

    congress_id = Column(String(100), ForeignKey('congress.id'))
    congress = relationship("Congress", back_populates="academic")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

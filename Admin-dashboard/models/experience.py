from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from . import Base

class Experience(Base):
    __tablename__ = 'experience'
    id = Column(Integer, primary_key=True)


    condition= Column(String(20))
    place = Column(String(20))
    province = Column(String(20))
    sector = Column(String(20))
    position = Column(String(20))
    start_year = Column(Integer)
    end_year = Column(Integer)

    congress_id = Column(String(100), ForeignKey('congress.id'))
    congress = relationship("Congress", back_populates="experience")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

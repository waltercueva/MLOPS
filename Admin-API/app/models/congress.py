from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, DateTime, Text
from sqlalchemy.orm import relationship

from . import Base
from . import congress_law

class Congress(Base):
    __tablename__ = 'congress'
    id = Column(String(100), primary_key=True)
    name = Column(String(255))
    birthdate_year = Column(Integer)
    gender = Column(String(10))
    birth_province = Column(String(20))
    province = Column(String(20))
    party = Column(String(100))
    start = Column(DateTime)
    end = Column(DateTime)

    academic = relationship("Academic", back_populates="congress")
    experience = relationship("Experience", back_populates="congress")
    law = relationship(
        "Law",
        secondary=congress_law.CongressLaw,
        back_populates="congress")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

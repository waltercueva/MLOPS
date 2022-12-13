from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
import datetime

from . import Base
from . import congress_law


class Law(Base):
    __tablename__ = 'law'
    id = Column(String(20), primary_key=True)
    law_path = Column(String(255))
    summary = Column(String(4000))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    congress = relationship(
        "Congress",
        secondary=congress_law.CongressLaw,
        back_populates="law")

    topic = relationship("Topic", back_populates="law")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


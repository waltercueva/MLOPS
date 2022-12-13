from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from . import Base


CongressLaw = Table(
    'congress_law', Base.metadata,
    Column('law_id', String(20), ForeignKey('law.id')),
    Column('congress_id', String(100), ForeignKey('congress.id'))
)
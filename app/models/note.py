import datetime

from sqlalchemy import Column, Text, DateTime

from .base import Base


class Note(Base):
    __tablename__ = "notes"

    text = Column(Text, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now().replace(microsecond=0))

    def __init__(self, text: str):
        self.text = text

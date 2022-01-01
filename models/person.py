from sqlalchemy import Column, String, Integer, DateTime
from services.database.db import Base


class Person(Base):
    __tablename__ = "crm_person"

    person_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_names = Column(String)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)


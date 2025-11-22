from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    data = Column(JSON, nullable=False)

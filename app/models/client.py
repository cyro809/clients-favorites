from app.core.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)

    favorites = relationship("Favorite", back_populates="client", cascade="all, delete-orphan", lazy="selectin")
    

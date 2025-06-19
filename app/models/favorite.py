from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id', ondelete="CASCADE"), nullable=False)
    product_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    image = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    client = relationship("Client", back_populates="favorites")
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base

# User model
class User(Base):
    __tablename__ = 'users'
    UniqueID = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    age = Column(Integer)

    # Relationship to StudySet
    study_sets = relationship('StudySet', back_populates='user')

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', age={self.age})>"

# StudySet model
class StudySet(Base):
    __tablename__ = 'study_sets'
    UniqueID = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    name = Column(String, nullable=False)
    category = Column(String)
    completed = Column(Integer, default=0)
    created_at = Column(Date)
    User_ID = Column(Integer, ForeignKey('users.UniqueID'))  # Foreign key

    # Relationship to User
    user = relationship('User', back_populates='study_sets')

    def __repr__(self):
        return f"<StudySet(name='{self.name}', category='{self.category}', completed={self.completed})>"

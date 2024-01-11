from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    assessments = relationship('Assessment', back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    assessments = relationship('Assessment', back_populates='teacher')

class Assessment(Base):
    __tablename__ = 'assessments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    
    student = relationship('Student', back_populates='assessments')
    teacher = relationship('Teacher', back_populates='assessments')
    
    subject = Column(String())
    score = Column(Integer())





  
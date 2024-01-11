from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Teacher, Assessment

if __name__ == '__main__':
    engine = create_engine('sqlite:///student_assessment.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Student).delete()
    session.query(Teacher).delete()
    session.query(Assessment).delete()

    
    fake = Faker()

    
    teachers = []
    for i in range(11):
        teacher = Teacher(
            first_name =fake.first_name(),
            last_name=fake.last_name()
        )

        # add and commit individually to get IDs back
        session.add(teacher)
        session.commit()

        teachers.append(teacher)

    subjects = [
    "Computer Vision",
    "Cloud Computing",
    "Human-Computer Interaction",
    "Big Data Analytics",
    "Computer Ethics",
    "Blockchain Technology",
    "Parallel and Distributed Computing"]
    for i in range(50):
        student = Student(
            first_name =fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(student)
        session.commit()
        for i in range(7):
            ass = Assessment(
                student_id = student.id,
                teacher_id = teachers[random.randint(0,len(teachers)-1)].id,
                subject = subjects[random.randint(0,len(subjects)-1)],
                score = random.randint(29,93)
            )
            session.add(ass)
            session.commit()
    session.commit()
    session.close()

    
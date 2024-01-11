import sys
from models import Student,Teacher,Assessment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///student_assessment.db')
Session = sessionmaker(bind=engine)
session = Session()

def all_students():
    global session
    return session.query(Student).all()

def all_student_results():
    global session
    ans = {}
    results = session.query(Assessment).all()
    
    for result in results:
        avg_score = 0
        subjects = 0
        
        subjects_marks = session.query(Assessment).filter(Assessment.student_id == result.student_id).all()
        
        for subject_mark in subjects_marks:
            avg_score += subject_mark.score
            subjects += 1
        
        if subjects > 0:
            avg_score /= subjects
        
        ans[result.student_id] = avg_score
    
    return ans

def top_score_students():
    global session
    results=session.query(Assessment).all()
    top_student=results[0]
    for i in results:
        if top_student.score < i.score:
            top_student=i
    student=session.query(Student).filter(Student.id==top_student.student_id).first()
    name= student.first_name+" "+student.last_name
    return {name:top_student.score}

def teacher_of_top_score_student():
    global session
    results=session.query(Assessment).all()
    top_student=results[0]
    for i in results:
        if top_student.score < i.score:
            top_student=i
    
    teacher=session.query(Teacher).filter(Teacher.id==top_student.teacher_id).first()
    return f"{teacher.first_name} {teacher.last_name}"
def average_per_subject():
    global session
    results=session.query(Assessment).all()
    subject={}
    for i in results:
        scores=0
        count=0
        if i.subject in subject:
            continue
        for k in results:
            count +=1
            if k.subject == i.subject:
                scores+=k.score
        mean=scores/count
        subject[i.subject]=mean
    return subject
def frequency_of_students_per_subject():
    global session
    results=session.query(Assessment).all()
    subject={}
    for i in results:
        count=0
        if i.subject in subject:
            continue
        for k in results:
            if k.subject == i.subject:
                count+=1
        subject[i.subject]=count
    return subject
def subject_taken_by_more_students():
    frequency=frequency_of_students_per_subject()
    highest_subject="Parallel and Distributed Computing"
    for subject in frequency:
        if frequency[subject] > frequency[highest_subject]:
            highest_subject=subject
    return highest_subject





if __name__ == "__main__":
    while True:
        value = input("""
        Select option:
        1. print_all_students
        2. print_all_students_results
        3. print_top_score_student
        4. teacher_of_top_score_student
        5. average_per_subject
        6. frequency_of_students_per_subject
        7. subject_taken_by_more_students
        """)
        match value:
            case "1":
                students=all_students()
                for student in students:
                    print(f"Student id {student.id}:name {student.first_name} {student.last_name} ")
            case "2":
                results = all_student_results()
                print(results)
            case "3":
                results = top_score_students()
                print(results)
            case "4":
                results=teacher_of_top_score_student()
                print (results)
            case "5":
                results=average_per_subject()
                print(results)
            case "6":
                results=frequency_of_students_per_subject()
                print(results)
            case "7":
                results=subject_taken_by_more_students()
                print(results)
        end = input("click enter to continue or q  and enter for close ")
        print(end)
        if end == "q":
            break
            
            

                
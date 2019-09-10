from db import db_handle

class Base:
    def save(self):
        db_handle.db_save(self)

    @classmethod
    def select(cls,username):
        obj = db_handle.db_select(cls,username)
        return obj

class Admin(Base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def creat_school(self,school_name,school_addr):
        School(school_name,school_addr)

    def creat_teacher(self,teacher_name,password):
        Teacher(teacher_name,password)

    def creat_course(self,school_name,course_name):
        school_obj = School.select(school_name)
        Course(course_name)
        school_obj.add_course(course_name)

class Student(Base):
    def __init__(self,student_name,student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.student_course_list = []
        self.score = {}
        self.save()

    def choose_school(self,school_name):
        self.school = school_name
        self.save()

    def choose_course(self,course_name):
        self.student_course_list.append(course_name)
        self.save()

    def check_score(self):
        return self.score


class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.name = teacher_name
        self.pwd = teacher_pwd
        self.teacher_course_list = []
        self.save()

    def check_course(self):
        return self.teacher_course_list

    def choose_course(self,course_name):
        self.teacher_course_list.append(course_name)
        self.save()

    def check_student(self,course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self,course_name,student_name,score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()

class Course(Base):
    def __init__(self,course_name):
        self.name = course_name
        self.student_list = []
        self.save()

    def add_student(self,student_name):
        self.student_list.append(student_name)
        self.save()

class School(Base):
    def __init__(self,school_name,school_addr):
        self.name = school_name
        self.addr = school_addr
        self.school_course_list = []
        self.save()

    def add_course(self,course_name):
        self.school_course_list.append(course_name)
        self.save()
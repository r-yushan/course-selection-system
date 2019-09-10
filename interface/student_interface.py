from db import models

def register_interface(username,password):
    admin_obj = models.Student.select(username)
    if not admin_obj:
        models.Student(username,password)
        return True,f'{username}---注册成功'
    return False,'用户已存在'

def choose_school_interface(student_name,school_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False,'学生已选择学校'
    student_obj.choose_school(school_name)
    return True,'选择学校成功'

def get_course_interface(student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        school_name = student_obj.school
        school_obj = models.School.select(school_name)
        return school_obj.school_course_list
    else:
        return '请先选择学校'

def choose_course_interface(student_name,course_name):
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.student_course_list:
        return '课程已存在'

    student_obj.choose_course(course_name)
    course_obj = models.Course.select(course_name)
    course_obj.add_student(student_name)
    return f'{course_name}---课程选择成功'

def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    score_dic = student_obj.check_score()
    return score_dic
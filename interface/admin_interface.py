from db import models

def register_interface(username,password):
    admin_obj = models.Admin.select(username)

    if not admin_obj:
        models.Admin(username,password)
        return True,f'{username}---注册成功'
    return False,'用户已存在'

def creat_school_interface(admin_name,school_name,school_addr):
    school_obj = models.School.select(school_name)
    if not school_obj:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_school(school_name,school_addr)
        return True,'学校创建成功'
    return False,'学校已存在'

def creat_teacher_interface(admin_name,teacher_name,password='123'):
    teacher_obj = models.Teacher.select(teacher_name)
    if not teacher_obj:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_teacher(teacher_name,password)
        return True,f'{teacher_name}---老师创建成功'
    return False,'老师已存在'

def creat_course(admin_name,school_name,course_name):
    school_obj = models.School.select(school_name)
    if course_name not in school_obj.school_course_list:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_course(school_name,course_name)
        return True,f'{course_name}---创建课程成功'
    else:
        return False,'课程已存在'
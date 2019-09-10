import os
from conf import setting
from db import models

def login_interface(username,password,user_type):
    if user_type == 'admin':
        obj = models.Admin.select(username)

    elif user_type == 'student':
        obj = models.Student.select(username)

    elif user_type == 'teacher':
        obj = models.Teacher.select(username)

    else:
        print('没有权限')

    if not obj:
        return False,'用户不存在'

    if obj.pwd == password:
        return True,f'{username}---登录成功'
    else:
        print('密码错误')

def get_school_interface():
    school_path = os.path.join(setting.BASE_DB,'School')
    if os.path.exists(school_path):
        school_list = os.listdir(school_path)
        return school_list

def get_course_interface():
    course_path = os.path.join(setting.BASE_DB,'Course')
    if os.path.exists(course_path):
        course_list = os.listdir(course_path)
        return course_list
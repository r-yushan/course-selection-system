

def login_auth(role):
    def auth(func):
        from core import admin,student,teacher
        def inner(*args,**kwargs):
            if role == 'admin':
                if admin.admin_info.get('user'):
                    res = func(*args,**kwargs)
                    return res
                else:
                    admin.admin_login()

            elif role == 'student':
                if student.student_info.get('user'):
                    res = func(*args,**kwargs)
                    return res
                else:
                    student.student_login()

            elif role == 'teacher':
                if teacher.teacher_info.get('user'):
                    res = func(*args,**kwargs)
                    return res
                else:
                    teacher.teacher_login()

            else:
                print('权限不足')
        return inner
    return auth
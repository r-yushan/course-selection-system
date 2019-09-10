from interface import common_interface,admin_interface
from db import db_handle
from lib import common

admin_info = {'name':None}

def admin_register():
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()

        flag,msg = admin_interface.register_interface(username,password)
        print(msg)
        if flag:
            break

def admin_login():
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()

        flag, msg = common_interface.login_interface(username, password,user_type='admin')
        print(msg)
        if flag:
            admin_info['user'] = username
            break

@common.login_auth('admin')
def creat_school():
    while True:
        school_name = input('请输入学校名称>>>').strip()
        school_addr = input('请输入学校地址>>>').strip()

        flag,msg = admin_interface.creat_school_interface(admin_info['user'],school_name,school_addr)
        print(msg)
        if flag:
            break

@common.login_auth('admin')
def creat_teacher():
    while True:
        teacher_name = input('请输入老师的用户名>>>').strip()

        flag, msg = admin_interface.creat_teacher_interface(admin_info['user'], teacher_name)
        print(msg)
        if flag:
            break

@common.login_auth('admin')
def creat_course():
    while True:
        school_list = common_interface.get_school_interface()
        if not school_list:
            print('没有学校，请去创建')
            break
        for school in school_list:
            print(school)

        choice = input('请选择学校>>>').strip()

        if choice in school_list:
            school_name = choice
            course_name = input('请输入课程名称>>>').strip()
            flag,msg = admin_interface.creat_course(admin_info.get('user'),school_name,course_name)
            print(msg)
            if flag:
                break
        else:
            print('请输入存在的学校')

func_dic = {
    '1':admin_register,
    '2':admin_login,
    '3':creat_school,
    '4':creat_teacher,
    '5':creat_course,
}

def admin_view():
    while True:
        print('''
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程        
        ''')
        choice = input('请输入你想要的功能,按q退出>>>').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            continue
        func_dic[choice]()
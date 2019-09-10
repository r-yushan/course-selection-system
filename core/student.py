from interface import student_interface,common_interface
from lib import common

student_info = {'user':None}

def student_register():
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()
        flag,msg = student_interface.register_interface(username,password)
        print(msg)
        if flag:
            break

def student_login():
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()
        flag, msg = common_interface.login_interface(username, password,user_type='student')
        print(msg)
        if flag:
            student_info['user'] = username
            break

@common.login_auth('student')
def choose_school():
    while True:
        school_list = common_interface.get_school_interface()
        for school in school_list:
            print(school)
        choice = input('请选择学校>>>').strip()
        if choice in school_list:
            school_name = choice
            flag,msg = student_interface.choose_school_interface(student_info['user'],school_name)
            print(msg)
            if flag:
                break
        else:
            print('请选择存在的学校')
            continue


@common.login_auth('student')
def choose_course():
    course_list = student_interface.get_course_interface(student_info.get('user'))
    for course in course_list:
        print(course)

    choice = input('请输入你要选择的课程>>>').strip()
    if choice in course_list:
        course_name = choice
        msg = student_interface.choose_course_interface(student_info.get('user'),course_name)
        print(msg)
    else:
        print('请选择存在的课程')


@common.login_auth('student')
def check_score():
    score_dic = student_interface.check_score_interface(student_info.get('user'))
    print(score_dic)

func_dic = {
    '1':student_register,
    '2':student_login,
    '3':choose_school,
    '4':choose_course,
    '5':check_score,
}

def student_view():
    while True:
        print('''
        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩        
        ''')
        choice = input('请输入你想要的功能,按q退出>>>').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            continue
        func_dic[choice]()


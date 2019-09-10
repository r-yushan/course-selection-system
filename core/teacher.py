from interface import common_interface,teacher_interface
from lib import common

teacher_info = {'user':None}

def teacher_login():
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()
        flag, msg = common_interface.login_interface(username, password,user_type='teacher')
        print(msg)
        if flag:
            teacher_info['user'] = username
            break

@common.login_auth('teacher')
def check_course():
    course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
    print(course_list)

@common.login_auth('teacher')
def choose_course():
    while True:
        course_list = common_interface.get_course_interface()

        if not course_list:
            print('暂无课程')
            break

        for course in course_list:
            print(course)

        choice = input('请选择教授课程>>>').strip()
        if choice in course_list:
            course_name = choice
            flag,msg = teacher_interface.choose_course_interface(teacher_info.get('user'),course_name)
            print(msg)
            if flag:
                break
        else:
            print('请选择存在的课程')

@common.login_auth('teacher')
def check_student():
    while True:
        course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not course_list:
            print('暂无课程')
            break
        for course in course_list:
            print(course)

        choice = input('请选择你要查看的课程>>>').strip()
        if choice in course_list:
            course_name = choice
            flag,msg = teacher_interface.check_student_interface(teacher_info.get('user'),course_name)
            print(msg)
            if flag:
                break
            break
        else:
            print('请选择存在的课程')

@common.login_auth('teacher')
def modify_score():
    while True:
        course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not course_list:
            print('暂无课程')
            break
        for course in course_list:
            print(course)
        course_choice = input('请选择课程>>>').strip()
        if course_choice in course_list:
            course_name = course_choice
            course = teacher_interface.get_course_interface(course_name)
            student_list = course.student_list
            if not student_list:
                print('暂无学生')
                break
            for student in student_list:
                print(student)
            student_choice = input('请选择学生>>>').strip()
            if student_choice in student_list:
                student_name = student_choice
                score = input('请输入分数>>>').strip()
                flag,msg = teacher_interface.change_score_interface(teacher_info.get('user'),course_name,student_name,score)
                print(msg)
                if flag:
                    break

func_dic = {
    '1':teacher_login,
    '2':check_course,
    '3':choose_course,
    '4':check_student,
    '5':modify_score,
}

def teacher_view():
    while True:
        print('''
        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩  
        ''')
        choice = input('请输入你想要的功能,按q退出>>>').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            continue
        func_dic[choice]()
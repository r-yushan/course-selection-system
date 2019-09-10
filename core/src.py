from core import admin,student,teacher

func_dic = {
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view,
}

def run():
    while True:
        print('''
        请选择登录角色：
        1、管理员视图
        2、学生视图
        3、老师视图
        ''')
        choice = input('请选择角色,按q退出>>>')
        if choice == 'q':
            break
        if func_dic.get(choice):
            func_dic[choice]()
        else:
            print('没有该功能')
            continue
import tkinter as tk
import tkinter.messagebox
import pickle
from Tank_Wars import main

window = tk.Tk()
window.title('login')
window.geometry('300x200')
# 登陆界面
tk.Label(window, text='账户：').place(x=60, y=40)
tk.Label(window, text='密码：').place(x=60, y=90)

var_usr_name = tk.StringVar()
enter_usr_name = tk.Entry(window, textvariable=var_usr_name)
enter_usr_name.place(x=100, y=40)

var_usr_pwd = tk.StringVar()
enter_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
enter_usr_pwd.place(x=100, y=90)


# 登陆
def usr_log_in():
    # 输入框内容
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            users_info = pickle.load(usr_file)
    except:
        with open('usr_info.pickle', 'wb') as usr_file:
            users_info = {'admin': 'admin'}
            pickle.dump(users_info, usr_file)

    # 判断
    if usr_name in users_info:
        if usr_pwd == users_info[usr_name]:
            # 登陆成功
            window.destroy()
        else:
            tk.messagebox.showerror(message='ERROR!')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名不能为空！')


def usr_sign_quit():
    window.destroy()


def usr_sign_up():
    def signtowcg():
        NewName = new_name.get()
        NewPwd = new_pwd.get()
        ConfirPwd = pwd_comfirm.get()
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}
        if NewName in exist_usr_info:
            tk.messagebox.showerror(message='用户名存在！')
        elif NewName == '' and NewPwd == '':
            tk.messagebox.showerror(message='用户名和密码不能为空！')
        elif NewPwd != ConfirPwd:
            tk.messagebox.showerror(message='密码前后不一致！')
        else:
            exist_usr_info[NewName] = NewPwd
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(message='注册成功！')
                window_sign_up.destroy()

    # 新建注册窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x250')
    window_sign_up.title('sign_up')

    # 注册编辑框
    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    pwd_comfirm = tk.StringVar()

    tk.Label(window_sign_up, text='账户名：').place(x=70, y=40)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=140, y=40)

    tk.Label(window_sign_up, text='密码：').place(x=70, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=140, y=90)

    tk.Label(window_sign_up, text='确认密码：').place(x=70, y=140)
    tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*').place(x=140, y=140)
    # 确认注册
    bt_confirm = tk.Button(window_sign_up, text='确定', command=signtowcg).place(x=160, y=180)


# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=110, y=140)

bt_signup = tk.Button(window, text='注册', command=usr_sign_up)
bt_signup.place(x=160, y=140)

window.wait_window(window=window)
main()

window.mainloop()

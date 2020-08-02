import random


def gen_chk_code():
    chk_code = str(random.randint(100000, 999999))
    print(f"您的验证码：{chk_code}")
    return chk_code


def login():
    chk = gen_chk_code()
    input_username = input("输入用户名：")
    input_passwd = input("输入密码：")
    input_chk = input("输入验证码：")

    with open("UserPass.txt", encoding="utf-8") as userpass:
        data = userpass.readlines()
        username = data[0].strip()
        passwd = data[1].strip()

        if input_username == username and input_passwd == passwd and input_chk == chk:
            print("登录成功！")
            return True
        else:
            print("登录失败，请重试！")
            return False


def manage():
    while 1:
        d = input("输入指令：")
        if d == "add":
            add()
            lookfor()
        elif d == "watch":
            lookfor()
        elif d == "quit":
            break
        elif d == "help":
            print("add, watch, quit")
        else:
            print("Command Not Found, Type 'help' to watch available commands.")


def lookfor():
    pass


def add():
    pass


for i in range(3):
    if login():
        # 管理开始
        break
else:
    print("失败3次，请稍后再试。")

manage()

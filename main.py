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

    with open("data/UserPass.txt", encoding="utf-8") as userpass:
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
        elif d == "count":
            count()
        elif d == "quit":
            break
        elif d == "help":
            print("add 添加, watch 查看, count数量, quit退出")
        else:
            print(f"Command '{d}' Not Found, Type 'help' to watch available commands.")


def lookfor():
    with open("data/ProductsData.txt", encoding="utf-8") as products:
        data = products.readlines()
        for line in data:
            print(line.strip())

def count():
    with open("data/ProductsData.txt", encoding="utf-8") as products:
        data = products.readlines()
        print(len(data))

def add():
    num = input("商品编号：") + ","
    name = input("商品名称：") + ","
    tp = input("类别：") + ","
    code = input("商品条码：") + ","
    am = input("数量：")
    with open("data/ProductsData.txt", encoding="utf-8", mode="a") as products:
        products.write(num + name + tp + code + am + "\n")

for i in range(3):
    if login():
        # 管理开始
        break
else:
    print("失败3次，请稍后再试。")

manage()

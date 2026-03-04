account = {}

while True:
    inp = input("請輸入操作選項(a 註冊,b 登入,c 離開)?")

    if inp not in ["a", "b", "c"]:
        print("無效的選項，請重新輸入")
        continue

    if inp == "c":
        print("離開程式")
        break

    if inp == "a":
        name = input("請輸入帳號:")
        if name in account:
            print("帳號已存在，請重新輸入")
            continue
        password = input("請輸入密碼:")
        account[name] = password
        print("註冊成功")
    elif inp == "b":
        name = input("請輸入帳號:")
        if name in account:
            password = input("請輸入密碼:")
            if account[name] == password:
                print("登入成功")
            else:
                print("密碼錯誤，請重新輸入")
        else:
            print("帳號不存在，請重新輸入")
    else:
        print("無效的選項，請重新輸入")

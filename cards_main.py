# 无限循环，有用户主动退出
while True:
    # TODO (zhuojiabin)显示功能菜单

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是[%s]" % action_str)

    #123针对名片的操作
    if action_str in ["1","2","3"]:
        #新增名片
        if action_str =="1":
            pass
        #显示全部
        if action_str =="2":
            pass
        #查询名片
        if action_str =="3":
            pass
        pass
    #0 退出系统
    elif action_str =="0":
        print("欢迎再次使用【名片管理系统】")
        break
        #如果在开发程序时，不希望立刻编写分支内部的代码
        #可以使用pass关键字，表示一个占位符，能够保证程序的代码
        #程序运行时，pass关键字不会执行任何操作
        pass

    #其他内容输入错误，需要提示用户
    else:
        print("您输入的内容错误，请重新输入")
        print("***************************************************")

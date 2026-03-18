def healthy_info():
    """功能界面"""
    print("------健康指标------")
    print("1.BMI(身体质量指数)")
    print("2.体脂率")
    print("3.腰臀比")
    print("4.退出系统")
def bmi_info():
    """BMI测量"""
    try:
        name=input("请输入你的姓名：")
        weight=float(input("请输入你的体重(公斤)："))
        height=float(input("请输入你的身高(米)："))
        bmi1=weight/(height*height)
        bmi=round(bmi1,2)
        if 0 < bmi < 18.5:
            print(f"{name}的BMI为{bmi},过轻")
        elif 18.5 <= bmi <= 24:
            print(f"{name}的BMI为{bmi},正常")
        elif 24 < bmi <= 27.9:
            print(f"{name}的BMI为{bmi},超重")
        elif bmi > 27.9:
            print(f"{name}的BMI为{bmi},肥胖")
        else:
            return
        with open("BMI.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{name}\t体重为{weight}公斤\t身高为{height}米\tBMI为{bmi}")
    except ValueError:
        print("格式异常！")
    except ZeroDivisionError:
        print("身高不能为0！")
def bfp_info():
    """体脂率的测定"""
    try:
        name = input("请输入你的姓名：")
        gender=int(input("你的性别是(填boy(1)或者girl(0))："))
        if gender==1:
            bmi=float(input("请输入你的BMI："))
            age=float(input("请输入你的年龄："))
            bfp10=1.2*bmi+0.23*age-10.8-5.4
            bfp1=round(bfp10,2)
            if 0 < bfp1 < 10:
                print(f"{name}的体脂率为{bfp1},瘦了！")
            elif 10 <= bfp1 <= 20:
                print(f"{name}的体脂率为{bfp1},健康标准！")
            elif 20 < bfp1 < 25:
                print(f"{name}的体脂率为{bfp1},超重！")
            elif 25 <= bfp1 < 100:
                print(f"{name}的体脂率为{bfp1},肥胖！")
            else:
                return
            with open("体脂率.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{name}\t性别:男\tBMI为{bmi}\t年龄为{age}\t体脂率为{bfp1}")
        if gender == 0:
            bmi = float(input("请输入你的BMI："))
            age = float(input("请输入你的年龄："))
            bfp00 = 1.2 * bmi + 0.23 * age - 5.4 - 1.3
            bfp0 = round(bfp00,2)
            if 0 < bfp0 < 18:
                print(f"{name}的体脂率为{bfp0},瘦了！")
            elif 18 <= bfp0 <= 28:
                print(f"{name}的体脂率为{bfp0},健康标准！")
            elif 28 < bfp0 <= 30:
                print(f"{name}的体脂率为{bfp0},超重！")
            elif 30 < bfp0 < 100:
                print(f"{name}的体脂率为{bfp0},肥胖！")
            else:
                return
            with open("体脂率.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{name}\t性别:女\tBMI为{bmi}\t年龄为{age}\t体脂率为{bfp0}")
    except ValueError:
        print("格式异常！")
def whr_info():
    """腰臀比测定"""
    try:
        name = input("请输入你的姓名：")
        gender = int(input("你的性别是(填boy(1)或者girl(0))："))
        if gender == 1:
            wc=float(input("请输入你的腰围："))
            hc=float(input("请输入你的臀围："))
            whr1=wc/hc
            whr=round(whr1,2)
            if 0 < whr < 0.9:
                print(f"{name}的腰臀比为{whr},健康！")
            elif 0.9 <= whr < 1:
                print(f"{name}的腰臀比为{whr},腹部肥胖！")
            else:
                return
            with open("腰臀比.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{name}\t性别:男\t腰围为{wc}\t臀围为{hc}\t腰臀比为{whr}")
        if gender == 0:
            wc=float(input("请输入你的腰围："))
            hc=float(input("请输入你的臀围："))
            whr0=wc/hc
            whr=round(whr0,2)
            if 0 < whr < 0.85:
                print(f"{name}的腰臀比为{whr},健康！")
            elif 0.85 <= whr < 1:
                print(f"{name}的腰臀比为{whr},腹部肥胖！")
            else:
                return
            with open("腰臀比.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{name}\t性别:女\t腰围为{wc}\t臀围为{hc}\t腰臀比为{whr}")
    except ValueError:
        print("格式异常！")
while True:
    try:
        healthy_info()
        choice1=int(input("请选择功能："))
    except ValueError:
        print("请不要乱输入！")
        continue
    if choice1==1:
        bmi_info()
    elif choice1==2:
        bfp_info()
    elif choice1==3:
        whr_info()
    elif choice1==4:
        exit_info=input("你是否退出？yes or no：")
        if exit_info=="yes":
            break
        elif exit_info=="no":
            continue
        else:
            print("请不要乱输入！")
    else:
        print("序号异常，请重新输入序号！")
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry("500x500")
root.title("功能界面")
def bmi_info():
    """BMI界面"""
    top1=tk.Toplevel()
    top1.geometry("500x500")
    #名字
    name1_label=tk.Label(top1,text="名字:")
    name1_label.place(x=100,y=50)
    name1=tk.Entry(top1,width=30)
    name1.place(x=140,y=50)
    #体重
    weight1_label=tk.Label(top1,text="体重:")
    weight1_label.place(x=100,y=125)
    weight1=tk.Entry(top1,width=30)
    weight1.place(x=140,y=125)
    #身高
    height1_label=tk.Label(top1,text="身高:")
    height1_label.place(x=100,y=200)
    height1=tk.Entry(top1,width=30)
    height1.place(x=140,y=200)
    #显示屏
    label1=tk.Label(top1,text="请输入数据！")
    label1.place(x=200,y=300)
    def click1():
        """BMI计算和判断"""
        name=name1.get()
        weight=float(weight1.get())
        height=float(height1.get())
        bmi1 = weight / (height * height)
        bmi = round(bmi1, 2)
        if 0 < bmi < 18.5:
            label1.config(text=f"{name}的BMI为{bmi},过轻")
        elif 18.5 <= bmi <= 24:
            label1.config(text=f"{name}的BMI为{bmi},正常")
        elif 24 < bmi <= 27.9:
            label1.config(text=f"{name}的BMI为{bmi},超重")
        elif bmi > 27.9:
            label1.config(text=f"{name}的BMI为{bmi},肥胖")
        else:
            tk.messagebox.showwarning("警告",message="你输入的数据异常！")
    btn1=tk.Button(top1,text="确定",command=click1,font=("Arial",20,"bold"))
    btn1.place(x=120,y=400)
    btn11=tk.Button(top1,text="退出",command=top1.destroy,font=("Arial",20,"bold"))
    btn11.place(x=300,y=400)
    top1.mainloop()
def bfp_info():
    """体脂率计算"""
    top2 = tk.Toplevel()
    top2.geometry("500x500")
    #名字
    name2_label = tk.Label(top2, text="名字:")
    name2_label.place(x=100, y=50)
    name2 = tk.Entry(top2, width=30)
    name2.place(x=140, y=50)
    #性别
    gender1_label=tk.Label(top2,text="性别:")
    gender1_label.place(x=100,y=125)
    gender1 = tk.Entry(top2, width=30)
    gender1.place(x=140, y=125)
    #BMI值
    bmi1_label=tk.Label(top2,text="BMI:")
    bmi1_label.place(x=100,y=200)
    bmi1 = tk.Entry(top2, width=30)
    bmi1.place(x=140, y=200)
    #年龄
    age1_label=tk.Label(top2,text="年龄:")
    age1_label.place(x=100,y=275)
    age1 = tk.Entry(top2, width=30)
    age1.place(x=140, y=275)
    #显示屏
    label2 = tk.Label(top2, text="请输入数据！")
    label2.place(x=200,y=350)
    #计算
    def click2():
        """体脂率的计算和判断"""
        if gender1.get() == "男":
            name=name2.get()
            gender=gender1.get()
            bmi=float(bmi1.get())
            age=float(age1.get())
            bfp1=1.2 * bmi + 0.23 * age - 10.8 - 5.4
            bfp0=round(bfp1,2)
            if 0 < bfp0 < 10:
                label2.config(text=f"{name},性别{gender},他的体脂率为{bfp0},瘦了！")
            elif 10 <= bfp0 <= 20:
                label2.config(text=f"{name},性别{gender},他的体脂率为{bfp0},健康标准！")
            elif 20 < bfp0 <= 25:
                label2.config(text=f"{name},性别{gender},他的体脂率为{bfp0},超重！")
            elif bfp0 > 25:
                label2.config(text=f"{name},性别{gender},他的体脂率为{bfp0},肥胖！")
            else:
                tk.messagebox.showwarning("警告", message="你输入的数据异常！")
        if gender1.get() == "女":
            name=name2.get()
            gender=gender1.get()
            bmi=float(bmi1.get())
            age=float(age1.get())
            bfp1=1.2 * bmi + 0.23 * age - 5.4 - 1.3
            bfp0=round(bfp1,2)
            if 0 < bfp0 < 18:
                label2.config(text=f"{name},性别{gender},她的体脂率为{bfp0},瘦了！")
            elif 18 <= bfp0 <= 28:
                label2.config(text=f"{name},性别{gender},她的体脂率为{bfp0},健康标准！")
            elif 28 < bfp0 <= 30:
                label2.config(text=f"{name},性别{gender},她的体脂率为{bfp0},超重！")
            elif bfp0 > 30:
                label2.config(text=f"{name},性别{gender},她的体脂率为{bfp0},肥胖！")
            else:
                tk.messagebox.showwarning("警告", message="你输入的数据异常！")
    btn2 = tk.Button(top2, text="确定", command=click2,font=("Arial",20,"bold"))
    btn2.place(x=120, y=420)
    btn21 = tk.Button(top2, text="退出", command=top2.destroy, font=("Arial", 20, "bold"))
    btn21.place(x=300, y=420)
    top2.mainloop()
def whr_info():
    top3 = tk.Toplevel()
    top3.geometry("500x500")
    # 名字
    name3_label = tk.Label(top3, text="名字:")
    name3_label.place(x=100, y=50)
    name3 = tk.Entry(top3, width=30)
    name3.place(x=140, y=50)
    # 性别
    gender2_label = tk.Label(top3, text="性别:")
    gender2_label.place(x=100, y=125)
    gender2 = tk.Entry(top3, width=30)
    gender2.place(x=140, y=125)
    # 腰围
    wc1_label = tk.Label(top3, text="腰围:")
    wc1_label.place(x=100, y=200)
    wc1 = tk.Entry(top3, width=30)
    wc1.place(x=140, y=200)
    # 臀围
    hc1_label = tk.Label(top3, text="臀围:")
    hc1_label.place(x=100, y=275)
    hc1 = tk.Entry(top3, width=30)
    hc1.place(x=140, y=275)
    # 显示屏
    label3 = tk.Label(top3, text="请输入数据！")
    label3.place(x=200, y=350)
    def click3():
        """腰臀比的计算和判定"""
        if gender2.get()=="男":
            name=name3.get()
            wc=float(wc1.get())
            hc=float(hc1.get())
            whr1 = wc / hc
            whr = round(whr1, 2)
            if 0 < whr < 0.9:
                label3.config(text=f"{name},性别{gender2},他的腰臀比为{whr},健康！")
            elif 0.9 <= whr < 1:
                label3.config(text=f"{name},性别{gender2},他的腰臀比为{whr},腹部肥胖！")
            else:
                tk.messagebox.showwarning("警告", message="你输入的数据异常！")
        if gender2.get()=="女":
            name=name3.get()
            wc=float(wc1.get())
            hc=float(hc1.get())
            whr0 = wc / hc
            whr = round(whr0, 2)
            if 0 < whr < 0.85:
                label3.config(text=f"{name},性别{gender2},她的腰臀比为{whr},健康！")
            elif 0.85 <= whr < 1:
                label3.config(text=f"{name},性别{gender2},她的腰臀比为{whr},腹部肥胖！")
            else:
                tk.messagebox.showwarning("警告", message="你输入的数据异常！")
    btn3=tk.Button(top3,text="确定",command=click3,font=("Arial",20,"bold"))
    btn3.place(x=120, y=420)
    btn31=tk.Button(top3,text="退出",command=top3.destroy,font=("Arial",20,"bold"))
    btn31.place(x=300, y=420)
    top3.mainloop()
btn1=tk.Button(root,text="BMI",command=bmi_info,font=("Arial",20),width=6)
btn1.place(x=100, y=100)
btn2=tk.Button(root,text="体脂率",command=bfp_info,font=("Arial",20),width=6)
btn2.place(x=100, y=300)
btn3=tk.Button(root,text="腰臀比",command=whr_info,font=("Arial",20),width=6)
btn3.place(x=300, y=100)
btn4=tk.Button(root,text="退出",command=root.destroy,font=("Arial",20),width=6)
btn4.place(x=300, y=300)
root.mainloop()

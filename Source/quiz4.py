#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'NERO'

#导入 Tkinter 库
from tkinter import *          #Tk, ttk//import tkinter

class QuizGUI(object):         #新建类QuizGUI，没有继承
    answer = 0                  #结果变量初始化
    menu = 'Quiz4'              #题目
    def __init__(self):             #通过__init__方法绑定属性，self指向创建的实例本身
        # 创建主窗口,用于容纳其它组件
        self.root = Tk()

        # 给主窗口设置标题内容
        self.root.title("这是一个标题")

        # 创建一个标签控件并显示
        Label(self.root, text=self.menu).pack()

        # 创建一个输入框,并设置尺寸
        self.input = Entry(self.root, width=30)
        self.input.pack()

        # 创建一个回显列表
        self.display_info = Listbox(self.root, width=50)
        self.display_info.pack()

        # 创建一个查询结果的按钮
        Button(self.root, command=self.quiz, text="Start").pack()

    # 根据quiz处理
    def quiz(self):                #定义方法(处理函数)
        # 获取输入信息
        self.input_value = self.input.get()

        # 创建临时列表
        temp_info = [ "Answer:" , str(self.input_value)]
        # 清空回显列表可见部分,类似clear命令
        for item in range(10):
            self.display_info.insert(0, "")

        # 为回显列表赋值
        for item in temp_info:
            self.display_info.insert(0, item)

def main():
    # 初始化对象，建立实例window
    window = QuizGUI()
    # 主程序执行
    mainloop()
    pass


if __name__ == "__main__":          #直接运行模块时__name__为__main__，被调用条件不成立，模块测试用
    main()
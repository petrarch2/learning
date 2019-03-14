#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding:utf-8 -*

#导入 Tkinter 库
from tkinter import *          #Tk, ttk//import tkinter

answer = 0                  #结果变量初始化

window = Tk()               #创建窗口
Label( window, text='Quiz4' ).grid()        #创建一个标签控件并显示

listb = Listbox(window)     #创建一个列表组件
listb.insert(0,answer)      #列表组件中插入数据
listb.insert(0,4)
listb.grid()                #把组件放到主窗口中

window.mainloop()           #进入消息循环


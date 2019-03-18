'''
Created on 2019年3月15日

@author: NERO
'''

import tkinter,os
from PIL import Image,ImageTk
from tkinter import filedialog

def GetPicL(pdir):  # 读取图片文件列表
    _pics = []
    for parent, dirnames, filenames in os.walk(pdir):
        for filename in filenames:
            if (filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG')):
                _pics.append(os.path.join(parent, filename))  # 保存PIC路径信息到列表
        #  print os.path.join(parent,filename)        #DEBUG
    return _pics

def Resize(w, h, w_box, h_box, pil_image):  # 缩放图片
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

def ShowPic(value):  # 显示图片
    global postion
    if (value == 1):
        if (postion > 0):
            postion = postion - 1
    if (value == 2):
        if (postion < len(pics) - 1):
            postion = postion + 1
    pil_image = Image.open(pics[postion])  # 按游标打开文件
    w, h = pil_image.size  # 取得文件像素大小
    pil_image_resized = Resize(w, h, w_box, h_box, pil_image)  # 按显示区域比例缩放，返回缩放后图片
    tk_img = ImageTk.PhotoImage(pil_image_resized)  # 缩放后文件，转化为ImageTk
    imglabel.configure(image=tk_img)  # 这是label类型为 tk-img类型image
    imglabel.image = tk_img  # 设置label显示的图片

    title['text'] = pics[postion]  # 设置图片标题
    title.pack(fill="x", expand=1)

    print(pics[postion])
    return True

def Repos(value):
    global postion
    postion = value
    ShowPic(2)
    
if __name__ == '__main__':
    MainForm = tkinter.Tk()  # 创建主窗体
    MainForm.title("漫画浏览器")  # 窗体标题

    """读配置文件"""
    rdir = tkinter.filedialog.askdirectory()
    #rdir = 'C:\Users\Administrator\Desktop\s'  # 图片根目录，限制图片<=3层
    w_box = MainForm.winfo_screenwidth()#1360  # 图片显示大小
    h_box = MainForm.winfo_screenheight()#760
    postion = 0
    
    '''读配置文件 结束'''
    pics = []  # PIC文件路径列表
    pics = GetPicL(rdir)  # 获取PIC文件路径列表
#     new_crazy = int(''.join(filter(str.isdigit, crazystring)))
    pics.sort(key=lambda x: ''.join(filter(str.isdigit, os.path.basename(x))))  # 按文件名末尾数字排序
    
    ''' 标题'''
    title = tkinter.Label(MainForm, text="", fg='blue', bg='gray', font='Helvetica -18 bold')
    title.pack(fill="x", expand=1)
            
    ''' 按钮'''
    tkinter.Button(MainForm, text='第一张', command=lambda: Repos(-1)).pack(side='top')

    tkinter.Button(MainForm, text='上一张', command=lambda: ShowPic(1)).pack(side='left')

    tkinter.Button(MainForm, text='下一张', command=lambda: ShowPic(2)).pack(side='right')

    ''' 图框'''
    imglabel = tkinter.Label(MainForm, image="", width=w_box, height=h_box)
    imglabel.pack(padx=15, pady=15)
    
    '''按键事件绑定，绑定键盘方向键'''
    MainForm.bind('<Left>', lambda x: ShowPic(1))
    MainForm.bind('<Right>', lambda x: ShowPic(2))

    ShowPic(1)
    MainForm.mainloop()

    #pyinstaller -w -F test_reader.py
    #-F：是直接生成单独的exe文件，不附带各种依赖文件的
    #-c：生成的exe文件打开方式为控制台打开
    #-w：这个和上面的-c对应，如果你的程序是有ui的，那就用这个-w。这样不会出现控制台，直接是你的ui
    #-I：给你的exe文件添加一个图标，后面要紧接着你想要的ico文件
    #-p：后面紧跟着你要指定的模块搜索路径

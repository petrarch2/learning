'''
Created on 2019年3月15日

@author: NERO
'''
'''
Created on ${date}

@author: ${user}
'''
import tkinter
import os

def GetPicL(pdir):  # 读取图片文件列表
    _pics = []
    for parent, dirnames, filenames in os.walk(pdir):
        for filename in filenames:
            _pics.append(os.path.join(parent, filename))  # 保存PIC路径信息到列表
        #  print os.path.join(parent,filename)        #DEBUG
    return _pics

if __name__ == '__main__':    
    MainForm = tkinter.Tk()  # 创建主窗体
    MainForm.title("漫画浏览器")  # 窗体标题
    
    """读配置文件"""
    rdir = '/Users/NERO/Documents/test_reader'
#     rdir = 'C:\Users\Administrator\Desktop\s'  # 图片根目录，限制图片<=3层
    w_box = 1360  # 图片显示大小
    h_box = 760
    
    '''读配置文件 结束'''
    pics = []  # PIC文件路径列表
    pics = GetPicL(rdir)  # 获取PIC文件路径列表
    pics.sort(key=lambda x: int(filter(str.isdigit, os.path.basename(x))))  # 按文件名末尾数字排序

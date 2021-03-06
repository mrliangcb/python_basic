#coding=utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

'''
信号传参类型
pyqtSignal()                               #无参数信号
pyqtSignal(int)                            # 一个参数(整数)的信号 
pyqtSignal([int],[str]                     # 一个参数(整数或者字符串)重载版本的信号
pyqtSignal(int,str)                        #二个参数(整数,字符串)的信号 
pyqtSignal([int,int],[int,str])          #二个参数([整数,整数]或者[整数,字符串])重载版本
'''


class Mythread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(str,list)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 下面的初始化方法都可以，有的python版本不支持
        #  super(Mythread, self).__init__()

    def run(self):
        for i in range(2000000):
            # 发出信号
            print(12)
            a=[i,i+1]
            self.breakSignal.emit(str(i),a)
            # 让程序休眠
            time.sleep(0.3)



app = QApplication([])
dlg = QDialog()
dlg.resize(400, 300)
dlg.setWindowTitle("自定义按钮测试")
dlgLayout = QVBoxLayout()
dlgLayout.setContentsMargins(40, 40, 40, 40)
btn = QPushButton('测试按钮')
dlgLayout.addWidget(btn)
dlgLayout.addStretch(40)
dlg.setLayout(dlgLayout)
dlg.show()    

def chuli(a,s):
        # dlg.setWindowTitle(s)
        btn.setText(a+str(s[0]*10))
    

    # 创建线程
thread = Mythread()
# # 注册信号处理函数
thread.breakSignal.connect(chuli)
# # 启动线程
thread.start()
dlg.exec_()
app.exit()

import os
import sys
import random

from PIL import Image, ImageQt
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QApplication

from qtdes import Ui_Form


shuzimoban = Image.open("pic/shuzimoban.jpg")  # 41*68

pic_save_path = os.path.join(os.path.expanduser('~'), "Desktop", "output1.jpg")
pic_save_path2 = os.path.join(os.path.expanduser('~'), "Desktop", "output2.jpg")
pic_save_path3 = os.path.join(os.path.expanduser('~'), "Desktop", "output3.jpg")
def str2pic(setdata,x_len,y_len):
    datalen=len(setdata)*x_len
    whiteback = Image.new('RGB', (datalen, y_len), color=(255, 255, 255) )
    index_setdate=0
    for i in range(len(setdata)):
            s_num = int(setdata[i])
            whiteback.paste(shuzimoban.crop((s_num * x_len, 0, (s_num + 1) * x_len, y_len)),
                            (index_setdate, 0))
            index_setdate = index_setdate + x_len
    return whiteback




if __name__ == '__main__':
    s='10000'+str(random.randint(1000,9999))
    a=str2pic(s)
    a.save(pic_save_path)
    s='10029363'+str(random.randint(1000,9999))
    a=str2pic(s)
    a.save(pic_save_path2)
    s='20210331'+str(random.randint(10,20))+str(random.randint(10,59))+str(random.randint(10,59))
    a=str2pic(s)
    a.save(pic_save_path3)


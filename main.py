import os
import sys

from PIL import Image, ImageQt
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QApplication

from qtdes import Ui_Form

shijianmaohao = Image.open("picsrc/shijianmaoh.jpg")  # 22*58
henggang = Image.open("picsrc/heng.jpg")  # 31*58
s_size_num = Image.open("picsrc/s_size_font.jpg")  # 38*58
b_size_num = Image.open("picsrc/b_size_font.jpg")  # 45*71
date2_num = Image.open("picsrc/date2_num.jpg")  # 57*84
da_pic = Image.open("picsrc/da.jpg")  # 117*72
oms_he_pic = Image.open("picsrc/oms_he.jpg")  # 298*63

kongge = Image.open("picsrc/kongge.jpg")  # 22*58
# self.fapian = Image.open("picsrc/e1369.jpg")  # 3024*2784
setdate = "2021-12-17 11:38:54"
# whiteback_im = whiteback.copy()
scale = 0.2

pic_save_path = os.path.join(os.path.expanduser('~'), "Desktop", "output.jpg")


class PYQT5mainclass(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(PYQT5mainclass, self).__init__(parent)
        self.setupUi(self)
        a = os.listdir("picsrc/门店")
        self.mendian_select.addItems(a)
        self.mendian = Image.open("picsrc/门店/" + self.mendian_select.currentText())

        a = os.listdir("picsrc/模板")
        self.moban_select.addItems(a)
        self.fapian = Image.open("picsrc/模板/" + self.moban_select.currentText())

        self.date_Edit.setDateTime(QDateTime.currentDateTime())
        self.moban_select.currentIndexChanged.connect(self.set_moban)
        self.mendian_select.currentIndexChanged.connect(self.set_mendian)
        self.Set_para_Button.clicked.connect(self.set_para)


        width = int(self.fapian.size[0] * scale)
        height = int(self.fapian.size[1] * scale)
        figure_resize = self.fapian.resize((width, height))
        self.Show_pic_label.setPixmap(ImageQt.toqpixmap(figure_resize))

        self.file_path = 'cfg.dat'
        self.data_ini_save=self.file_ini_read(self.file_path)

        self.DA_text.setText(self.data_ini_save[0])
        self.Date2_text.setText(self.data_ini_save[1])
        self.lineEdit_3.setText(self.data_ini_save[2])

    def file_ini_read(self,file_path):
        with open(file_path, 'r') as file:
            a = file.readlines()
            if len(a) < 3:
                a = ['1558924', '20201212', '00215187506902']
            else:
                for i in range(len(a)):
                    a[i] = a[i][:-1]
            return a

    def file_ini_write(self,file_path, s):
        with open(file_path, 'w') as file:
            file.write(s)

    def set_mendian(self):
        self.mendian = Image.open("picsrc/门店/" + self.mendian_select.currentText())
        self.fapian = Image.open("picsrc/模板/" + self.moban_select.currentText())
        self.fapian.paste(self.mendian, (288, 463))

        width = int(self.fapian.size[0] * scale)
        height = int(self.fapian.size[1] * scale)
        figure_resize = self.fapian.resize((width, height))
        self.Show_pic_label.setPixmap(ImageQt.toqpixmap(figure_resize))

    def set_moban(self):
        self.fapian = Image.open("picsrc/模板/" + self.moban_select.currentText())
        width = int(self.fapian.size[0] * scale)
        height = int(self.fapian.size[1] * scale)
        figure_resize = self.fapian.resize((width, height))
        self.Show_pic_label.setPixmap(ImageQt.toqpixmap(figure_resize))

    @staticmethod
    def str2pic(setdata, pictype):
        if pictype == 'date':
            copy_num_pic = s_size_num
            parat = (31, 22, 22, 38, 58)
            whiteback = Image.new('RGB', (660, 58), color=(255, 255, 255))
            index_setdate = 0
        elif pictype == 'date2':
            copy_num_pic = date2_num
            parat = (31, 22, 22, 57, 84)
            whiteback = Image.new('RGB', (470, 84), color=(255, 255, 255))
            index_setdate = 0
        elif pictype == 'da':
            copy_num_pic = b_size_num
            parat = (31, 22, 22, 45, 71)
            whiteback = Image.new('RGB', (430, 71), color=(255, 255, 255))
            whiteback.paste(da_pic, (0, 0))
            index_setdate = 117
        elif pictype == 'oms':
            copy_num_pic = s_size_num
            parat = (31, 22, 22, 38, 58)
            whiteback = Image.new('RGB', (900, 63), color=(255, 255, 255))
            whiteback.paste(oms_he_pic, (0, 0))
            index_setdate = 299
        else:
            copy_num_pic = s_size_num
            parat = (31, 22, 22, 38, 58)
            whiteback = Image.new('RGB', (660, 58), color=(255, 255, 255))
            index_setdate = 0

        for i in range(len(setdata)):
            if (setdata[i]) == '-':
                whiteback.paste(henggang, (index_setdate, 0))
                index_setdate = index_setdate + parat[0]
            elif (setdata[i]) == ' ':
                whiteback.paste(kongge, (index_setdate, 0))
                index_setdate = index_setdate + parat[1]
            elif (setdata[i]) == ':':
                whiteback.paste(shijianmaohao, (index_setdate, 0))
                index_setdate = index_setdate + parat[2]
            else:
                s_num = int(setdata[i])
                whiteback.paste(copy_num_pic.crop((s_num * parat[3], 0, s_num * parat[3] + parat[3], parat[4])),
                                (index_setdate, 0))
                index_setdate = index_setdate + parat[3]
        return whiteback

    def set_para(self):
        mydate_set = str(self.date_Edit.text())
        myda_set = str(self.DA_text.text())
        mydate2_set = str(self.Date2_text.text())
        myoms_set = str(self.lineEdit_3.text())
        mydate = self.str2pic(mydate_set, 'date')
        myda = self.str2pic(myda_set, 'da')
        mydate2 = self.str2pic(mydate2_set, 'date2')
        myoms = self.str2pic(myoms_set, 'oms')
        # output_pic=Image.new('RGB', (700, 400), color=(255, 255, 255))
        # output_pic.paste(mydate, (0, 0))
        # output_pic.paste(myda, (0, 100))
        # output_pic.paste(mydate2, (0, 200))
        # output_pic.paste(myoms, (0, 300))
        # output_pic.save('output.jpg')

        self.fapian.paste(mydate, (313, 612))
        self.fapian.paste(myda, (301, 1139))
        self.fapian.paste(mydate2, (920, 1137))
        self.fapian.paste(myoms, (315, 1354))
        width = int(self.fapian.size[0] * scale)
        height = int(self.fapian.size[1] * scale)
        figure_resize = self.fapian.resize((width, height))
        self.Show_pic_label.setPixmap(ImageQt.toqpixmap(figure_resize))
        self.fapian.save(pic_save_path)
        self.data_ini_save[0] = self.DA_text.text()
        self.data_ini_save[1] = self.Date2_text.text()
        self.data_ini_save[2] = self.lineEdit_3.text()
        s=str(self.data_ini_save[0])+'\n'+str(self.data_ini_save[1])+'\n'+str(self.data_ini_save[2])+'\n'
        self.file_ini_write(self.file_path,s)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = PYQT5mainclass()
    myshow.show()
    sys.exit(app.exec_())

    # mydate_set=input("\n请输入时间\n")
    # myda_set = str(input("\n请输入DA号\n"))
    # mydate2_set = str(input("\n请输入日期\n"))
    # myoms_set = str(input("\n请输入OMS单号\n"))
    #
    # mydate= str2pic(mydate_set,'date')
    #
    # myda= str2pic(myda_set,'da')
    # mydate2 = str2pic(mydate2_set,'date2')
    #
    # myoms= str2pic(myoms_set,'oms')
    #
    # output_pic=Image.new('RGB', (700, 400), color=(255, 255, 255))
    # output_pic.paste(mydate, (0, 0))
    # output_pic.paste(myda, (0, 100))
    # output_pic.paste(mydate2, (0, 200))
    # output_pic.paste(myoms, (0, 300))
    # output_pic.save('output.jpg')

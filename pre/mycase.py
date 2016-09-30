# -*- coding: utf-8 -*-
import os
import sys
# sys.path.append("../../report_test")
sys.path.append("./pre/")
from myexcel import myexcel
class mycase():
    def crt_case(self):
        fp = open("./suite/test_suite.py","a+")
        fp.truncate()
#--------------写文件头---------------------------------------------------------------------
        seq ='''# -*- coding: utf-8 -*-

import unittest
import serial
from myexcel import myexcel
from mycom import mycom
from time import sleep

class Test_LKJ(unittest.TestCase):
    def setUp(self):
        print "setup"
        '''
        fp.writelines(seq)
#--------------写函数体-------------------------------------------------------------------
        t = myexcel()
        num=t.get_rows()
        for i in range(1,num):
            t = myexcel()
            name=(t.read_data(i,0)).encode()
            seq ='''
    def test_%s(self):
        print u"正在执行第%s条测试用例： %s"
        t = myexcel()
        datas=t.read_data(%s,%s)
        serialport = serial.Serial("com1",9600,timeout=1)
        d=mycom().w_change(datas)
        serialport.write(d)
        while True:
            comdata =serialport.read(2)
            data=comdata
            sleep(0.5)
            if data=="55":
                break;
        serialport.close()
        excel_data1=[]
        excel_data2=[]
            '''%(i,i,name,i,1)
            fp.writelines(seq)
            seq ='''
        for j in range(1,9):
            excel_data1.append(t.read_data(%s,j+1))
            excel_data2.append(t.read_data(%s,j+9))
        '''%(i,i)
            fp.writelines(seq)
            seq='''
        self.assertEqual(excel_data1, excel_data2)


        '''
            fp.writelines(seq)
                

    
#---------------写结束部分--------------------------------------------------------------------

        seq ='''
    def tearDown(self):
        print u'本条用例测试完成'

if __name__ == '__main__':
    unittest.main()
        '''
        fp.writelines(seq)
        fp.close()


if __name__ == '__main__':
    case=mycase()
    case.crt_case()
# -*- coding: utf-8 -*-
import serial
from time import sleep
import sys,binascii,string
from myexcel import myexcel

class mycom:

    def sendcom_data(self):
        #循环发送表格内的数据
        datas=[]
        t = myexcel()
        datas=t.read_casedata()
        serialport = serial.Serial("com1",9600,timeout=1)

        for i in range(0,len(datas)) :
            d =bytes.binascii.b2a_hex(datas[i])
            #serialport.write(str(datas[i]).encode('utf-8'))
            serialport.write(d)
            while True:
                comdata =serialport.read(2)
                data=comdata
                sleep(0.5)
                if data=="55":
                    break;
        serialport.close()

    def w_change(self,datas):
        datas=datas.encode()
        data=datas.split()
        data=''.join(data)
        hexer =data.decode('hex')
        return hexer

    def sendcom_one(self,row,column):
        #向串口发送一个单元格的数据
        
        t = myexcel()
        datas=t.read_data(row,column)
        serialport = serial.Serial("com1",9600,timeout=1)
        datas=datas.encode()
        data=datas.split()
        data=''.join(data)
        hexer =data.decode('hex') 
        serialport.write(hexer)

        while True:
            comdata =serialport.read(2)
            data=comdata
            sleep(0.5)
            if data=="55":
                break;
        serialport.close()






if __name__ == '__main__':
    print "111"
    com =mycom()
    com.sendcom_one(1,1)
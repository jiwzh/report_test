# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import os ,time,datetime
import sys,binascii,string
sys.path.append("./pre/")
from myexcel import myexcel
from mycom import mycom
from mycase import mycase
import serial
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendmail(test_result):
    msgroot=MIMEMultipart()
    msgroot['subject']=u'测试报告'
    msgroot['from']='jiwz@hnthinker.com'
    msgroot['to']='jiwz@hnthinker.com'

    f = open(test_result,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msgroot.attach(msg)

    att=MIMEText(open('%s'%test_result,'rb').read(),'base64','gb2312')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']=('attachment;filename = "report.html"')
    msgroot.attach(att)
    try:
        smtp=smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login('jiwz@hnthinker.com','*****')
        smtp.sendmail(msgroot['from'],msgroot['to'],msgroot.as_string())
        smtp.quit()
        print u'邮件发送成功'
    except Exception, e:
        print str(e)
    

def read_result():
    result_dir = "./report/"
    result_lists = os.listdir(result_dir)
    result_lists.sort(
        key = lambda fn:os.path.getatime(result_dir + "\\" + fn)
        if not os.path.isdir(result_dir + "\\" + fn)
    else 0)
    print (u'最新的测试报告为：' + result_lists[-1])
    test_result = os.path.join(result_dir,result_lists[-1])
    print test_result
    sendmail(test_result)

def ceratsuit():
    case_list = "./suite/"
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        case_list,
        pattern='test_suite*.py',
        top_level_dir=None
    )
    for all_testcases in discover:
        for test_case in all_testcases:
            testsuit.addTest(test_case)
    print testsuit
    return testsuit

if __name__ == '__main__':
    case=mycase()
    case.crt_case()
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    result_name = "./report/" + now +'.html'
    fp = file(result_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream= fp,
        title= u'测试报告',
        description=u'测试结果'
    )
    runner.run(ceratsuit())
    fp.close()
    read_result()
    raw_input ("<enter>")

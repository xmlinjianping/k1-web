import unittest
import time
#加载测试文件  from 文件 import 类名
from testadd import testAdd
from testsub import testSub
import HTMLTestRunner

from  email.mime.text import MIMEText
from email.header import Header
import smtplib
import  os


#==========定义发送邮件=================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body =  f.read()
    f.close()
   #email模块主要负责构造邮件
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    msg['From'] = Header("林建平自动化测试")
    msg['To'] = Header("管理员")

    #smtplib模块主要负责发送邮件
    sender = '562289251@qq.com'
    receiver = 'linjianping@gengee.cn'
    smtpserver = 'smtp.qq.com'
    username = '562289251@qq.com'
    password = 'zhoqelfabouybcce'

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password) #注：这个密码不是登陆QQ邮箱的密码，而是授权码，开启SMTP服务后，会提示用手机发短信收授权码https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
    smtp.sendmail(sender, receiver, msg.as_string() )
    smtp.quit()
    print("email has send out")

#===========查找测试报告目录，找到最新生成的测试报告文件===========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

#构造测试集
#suite = unittest.TestSuite()
#suite.addTest(testAdd("test_add"))  #括号里是类，然后是类的方法
#suite.addTest(testSub("test_sub"))


if __name__ == "__main__":

    test_dir = './'
    test_report = "D:\\python\\src\\report"
    discouver = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename="D:\\python\\src\\report\\"+now+"_result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'功能测试报告',description=u'用例执行情况：')
    runner.run(discouver)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

    #使用discouver构造测试集
    #test_dir = './'
    #discouver = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #执行测试
    #runner=unittest.TextTestRunner()
    #runner.run(suite)
    #runner.run(discouver)


    #生成报告的模式
    #now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    #filename="D:\\python\\src\\report\\"+now+"_result.html"
    #fp=open(filename,'wb')
    #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'功能测试报告',description=u'用例执行情况：')
    #runner.run(suite)
    #fp.close()
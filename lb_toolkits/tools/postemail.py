# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : postemail.py

@Modify Time :  2022/12/21 14:16   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

class postemail() :

    def __init__(self, username, passwd, host="smtp.126.com"):

        stp = smtplib.SMTP()

        self.stp = smtplib.SMTP_SSL(host)#此段代码表示使用ssl协议，163邮箱用465或994端口，否则用25端口

        # 设置发件人邮箱的域名和端口，端口地址为25
        self.stp.connect(host, 465)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        self.stp.set_debuglevel(0)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        self.stp.login(username, passwd)

        self.msg = MIMEMultipart('related')
        self.msg['Date'] = time.ctime(time.time()) #设置时间
        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        # self.msg["From"] = "xxxx<xxx@126.com>"
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
        # self.msg["To"] = "xxxr<xxxx@163.com>"

    def set_header(self, content):
        ''' 邮件主题 '''

        # 设置邮件主题
        self.msg["Subject"] = Header(content, 'utf-8')

    def set_body(self, content):
        ''' 邮件正文内容 '''

        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        message_text = MIMEText(content, "plain", "utf-8")
        # 向MIMEMultipart对象中添加文本对象
        self.msg.attach(message_text)

    def add_image(self, imgname):
        '''  '''
        # 二进制读取图片
        with open(imgname,'rb') as fp :
            # 设置读取获取的二进制数据
            message_image = MIMEImage(fp.read())
        image_name = os.path.basename(imgname)

        # 添加图片文件到邮件信息当中去
        message_image.add_header("Content-Disposition",'attachment',
                                 filename=('gbk', '', os.path.basename(imgname)))
        self.msg.attach(message_image)


    def add_file(self, filename):
        # 构造附件
        atta = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        # 设置附件信息
        # atta["Content-Disposition"] = 'attachment; filename=%s' %(os.path.basename(filename).encode('gb2312'))
        atta.add_header("Content-Disposition",'attachment', filename=('gbk', '', os.path.basename(filename)))
        # 添加附件到邮件信息当中去
        self.msg.attach(atta)

    def send(self, sender, receivers):

        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        self.stp.sendmail(sender, receivers, self.msg.as_string())

        # 关闭SMTP对象
        self.stp.quit()
        print("成功邮件发送", receivers)










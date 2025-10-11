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
import re
import logging
import smtplib
import imaplib
import email
from email.mime.image import MIMEImage
from email.header import Header, decode_header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from imapclient import IMAPClient


SMTP_CONFIGS = {
    "163.com": {
        "name": "网易邮箱(163)",
        "server": "smtp.163.com",
        "port": 25,
        "notes": "需开启客户端授权并使用授权码登录"
    },
    "126.com": {
        "name": "网易邮箱(126)",
        "server": "smtp.126.com",
        "port": 25,
        "notes": "需开启客户端授权并使用授权码登录"
    },
    "qq.com": {
        "name": "QQ邮箱",
        "server": "smtp.qq.com",
        "port": 587,
        "notes": "需开启SMTP服务并使用授权码登录"
    },
    "sina.com": {
        "name": "新浪邮箱",
        "server": "smtp.sina.com",
        "port": 25,
        "notes": ""
    },
    "yahoo.com": {
        "name": "雅虎邮箱",
        "server": "smtp.mail.yahoo.com",
        "port": 587,
        "notes": "需使用应用专用密码"
    },
    "gmail.com": {
        "name": "Gmail",
        "server": "smtp.gmail.com",
        "port": 587,
        "notes": "需开启Less secure app access或使用应用专用密码"
    },
    "outlook.com": {
        "name": "Outlook/Hotmail",
        "server": "smtp.office365.com",
        "port": 587,
        "notes": "两步验证用户需使用应用专用密码"
    },
    "office365.com": {
        "name": "Outlook/Hotmail",
        "server": "smtp.office365.com",
        "port": 587,
        "notes": "两步验证用户需使用应用专用密码"
    },
}

# 常用邮箱IMAP服务器配置
IMAP_CONFIGS = {
    "gmail.com": {
        "name": "Gmail",
        "server": "imap.gmail.com",
        "port": 993,
        "notes": "需在设置中开启IMAP访问，两步验证用户需使用应用专用密码"
    },
    "outlook.com": {
        "name": "Outlook/Hotmail",
        "server": "imap-mail.outlook.com",
        "port": 993,
        "notes": "两步验证用户需使用应用专用密码"
    },
    "163.com": {
        "name": "网易163邮箱",
        "server": "imap.163.com",
        "port": 993,
        "notes": "需开启IMAP服务并使用授权码登录"
    },
    "126.com": {
        "name": "网易126邮箱",
        "server": "imap.126.com",
        "port": 993,
        "notes": "需开启IMAP服务并使用授权码登录"
    },
    "qq.com": {
        "name": "QQ邮箱",
        "server": "imap.qq.com",
        "port": 993,
        "notes": "需开启IMAP服务并使用授权码登录"
    },
    "sina.com": {
        "name": "新浪邮箱",
        "server": "imap.sina.com",
        "port": 993,
        "notes": ""
    },
    "yahoo.com": {
        "name": "雅虎邮箱",
        "server": "imap.mail.yahoo.com",
        "port": 993,
        "notes": "需使用应用专用密码"
    }
}


class EmailSender:
    def __init__(self, host, passwd, server=None, port=None):
        """初始化邮件发送器"""
        self.sender_email = host
        self.password = passwd
        self.smtp_server = server
        self.smtp_port = port
        self.server = None

        # 检查传入的参数信息
        self._checkinfo()

        # 连接服务
        self.connect()

    def _checkinfo(self):
        if '@' in self.sender_email:
            index = self.sender_email.index('@')
            emailType = self.sender_email[index+1:]
            if self.smtp_server is None and emailType in SMTP_CONFIGS :
                self.smtp_server = SMTP_CONFIGS[emailType]["server"]
            # else:
            #     raise Exception('传入正确的server【%s】' %(self.smtp_server))

            if self.smtp_port is None and emailType in SMTP_CONFIGS :
                self.smtp_port = SMTP_CONFIGS[emailType]["port"]
            # else:
            #     raise Exception('传入正确的port【%s】' %(self.smtp_port))
            print(self.sender_email, self.password)
            print(self.smtp_server, self.smtp_port)
        else:
            raise Exception('传入正确的host【%s】' %(self.sender_email))

    def connect(self):
        """连接到SMTP服务器"""
        try:
            # 连接到SMTP服务器
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.starttls()  # 启用TLS加密
            self.server.login(self.sender_email, self.password)
            print("成功连接到邮件服务器并登录")
            return True
        except Exception as e:
            print(f"连接或登录失败: {str(e)}")
            return False

    def add_attachment(self, msg, file_path):
        """向邮件添加附件"""
        if not os.path.isfile(file_path):
            print(f"警告: 文件 {file_path} 不存在，已跳过")
            return False

        try:
            # 读取文件内容
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # 编码为base64
            encoders.encode_base64(part)

            # 添加头信息
            filename = os.path.basename(file_path)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # 将附件添加到邮件
            msg.attach(part)
            print(f"已添加附件: {filename}")
            return True
        except Exception as e:
            print(f"添加附件 {file_path} 失败: {str(e)}")
            return False

    def send_email(self, recipient_emails, subject=None, body=None, attachment_paths=None):
        """发送邮件"""
        if not self.server:
            print("请先连接到邮件服务器")
            return False

        # 确保收件人是列表格式
        if isinstance(recipient_emails, str):
            recipient_emails = [recipient_emails]

        # 创建邮件对象
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = ", ".join(recipient_emails)
        msg["Subject"] = subject

        # 添加邮件正文
        if body is not None:
            msg.attach(MIMEText(body, "plain"))

        # 添加附件
        if attachment_paths:
            if isinstance(attachment_paths, str):
                attachment_paths = [attachment_paths]

            for path in attachment_paths:
                self.add_attachment(msg, path)

        try:
            # 发送邮件
            self.server.sendmail(
                self.sender_email,
                recipient_emails,
                msg.as_string()
            )
            print(f"邮件已成功发送到: {', '.join(recipient_emails)}")
            return True
        except Exception as e:
            print(f"发送邮件失败: {str(e)}")
            return False

    def disconnect(self):
        """断开与服务器的连接"""
        if self.server:
            self.server.quit()
            self.server = None
            print("已断开与邮件服务器的连接")

    def __del__(self):
        try:
            if self.server:
                self.server.quit()
                self.server = None
                print("已断开与邮件服务器的连接")
        except Exception as e:
            print(e)

class EmailReader:
    def __init__(self, host, passwd, server=None, port=None):
        """初始化邮件发送器"""
        self.email_address = host
        self.password = passwd
        self.imap_server = server
        self.imap_port = port
        self.client = None
        self.attachments_dir = r'E:\test'

        # 检查传入的参数信息
        self._checkinfo()

        # 连接服务
        self.connect()

    def read_emails(self, folder="INBOX", limit=10):
        """读取邮件，默认读取收件箱的最新10封邮件"""
        try:
            # 选择邮件文件夹
            self.client.select_folder(folder)

            # 搜索所有邮件并按日期排序
            email_ids = self.client.search(['ALL'])
            # 获取最新的limit封邮件
            if len(email_ids) > limit:
                email_ids = email_ids[-limit:]

            emails = []
            for email_id in email_ids:
                email_info = self.process_email(email_id)
                if email_info:
                    emails.append(email_info)
                    print(f"已处理邮件: {email_info['subject']}")

            return emails

        except Exception as e:
            print(f"读取邮件失败: {str(e)}")
            return []

    def search_emails(self, query, limit=10):
        """根据查询条件搜索邮件"""
        try:
            # 选择邮件文件夹
            self.client.select_folder('INBOX', readonly=True)

            # 搜索邮件
            email_ids = self.client.search(['ALL',
                                            [u'SINCE', datetime.date(2022, 3, 6)],])

            # 限制返回数量
            if len(email_ids) > limit:
                email_ids = email_ids[-limit:]

            emails = []
            for email_id in email_ids:
                email_info = self.process_email(email_id)
                if email_info:
                    emails.append(email_info)
                    print(f"已处理邮件: {email_info['subject']}")

            return emails

        except Exception as e:
            print(f"搜索邮件失败: {str(e)}")
            return []


    def _checkinfo(self):
        if '@' in self.email_address:
            index = self.email_address.index('@')
            emailType = self.email_address[index+1:]
            if self.imap_server is None and emailType in SMTP_CONFIGS :
                self.imap_server = IMAP_CONFIGS[emailType]["server"]
            # else:
            #     raise Exception('传入正确的server【%s】' %(self.smtp_server))

            if self.imap_port is None and emailType in SMTP_CONFIGS :
                self.imap_port = IMAP_CONFIGS[emailType]["port"]
            # else:
            #     raise Exception('传入正确的port【%s】' %(self.smtp_port))
            print(self.email_address, self.password)
            print(self.imap_server, self.imap_port)
        else:
            raise Exception('传入正确的host【%s】' %(self.sender_email))


    def connect(self):
        """连接到邮件服务器并登录"""
        try:
            # 连接到IMAP服务器
            self.client = IMAPClient(self.imap_server, ssl=True,port=993)

            # 登录邮箱
            self.client.login(self.email_address, self.password)

            self.client.id_({"name": "IMAPClient", "version": "2.1.0"})

            print(f"成功登录到 {self.imap_server}")
            return True
        except Exception as e:
            print(f"连接或登录失败: {str(e)}")
            if "authentication failed" in str(e).lower():
                print("提示: 可能需要使用授权码而非登录密码")
            return False

    def decode_str(self, s):
        """解码邮件中的字符串"""
        if not s:
            return ""
        value, charset = decode_header(s)[0]
        if isinstance(value, bytes):
            # 尝试解码，处理可能的编码问题
            try:
                if charset:
                    return value.decode(charset)
                else:
                    # 尝试常见编码
                    for encoding in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
                        try:
                            return value.decode(encoding)
                        except UnicodeDecodeError:
                            continue
                    return value.decode('utf-8', errors='replace')
            except:
                return str(value)
        return str(value)

    def get_email_body(self, msg):
        """获取邮件正文"""
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # 跳过附件
                if "attachment" in content_disposition:
                    continue

                # 文本内容
                if content_type == "text/plain" or content_type == "text/html":
                    try:
                        part_body = part.get_payload(decode=True)
                        # 尝试解码正文
                        for encoding in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
                            try:
                                body += part_body.decode(encoding)
                                break
                            except UnicodeDecodeError:
                                continue
                    except Exception as e:
                        print(f"解析正文出错: {str(e)}")
                        continue
        else:
            # 非多部分邮件
            content_type = msg.get_content_type()
            if content_type == "text/plain" or content_type == "text/html":
                try:
                    part_body = msg.get_payload(decode=True)
                    for encoding in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
                        try:
                            body = part_body.decode(encoding)
                            break
                        except UnicodeDecodeError:
                            continue
                except Exception as e:
                    print(f"解析正文出错: {str(e)}")

        return body

    def save_attachment(self, part, email_id):
        """保存邮件附件"""
        try:
            filename = part.get_filename()
            if filename:
                # 解码附件文件名
                filename = self.decode_str(filename)

                # 清理文件名中的特殊字符
                filename = re.sub(r'[\\/*?:"<>|]', "_", filename)

                # 创建每个邮件的附件目录
                email_attach_dir = os.path.join(self.attachments_dir, f"email_{email_id}")
                if not os.path.exists(email_attach_dir):
                    os.makedirs(email_attach_dir)

                # 保存附件
                filepath = os.path.join(email_attach_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f"已保存附件: {filepath}")
                return filepath
        except Exception as e:
            print(f"保存附件失败: {str(e)}")
        return None

    def process_email(self, email_id):
        """处理单封邮件，返回邮件信息和附件列表"""
        try:
            # 获取邮件内容
            messages = self.client.fetch([email_id], ['RFC822'])
            msg_data = messages[email_id]
            msg = email.message_from_bytes(msg_data[b'RFC822'])

            # 解析邮件头部信息
            subject = self.decode_str(msg["Subject"])
            from_email = self.decode_str(msg["From"])
            to_email = self.decode_str(msg["To"]) if msg["To"] else ""
            date = self.decode_str(msg["Date"])

            # 获取邮件正文
            body = self.get_email_body(msg)

            # 处理附件
            attachments = []
            if msg.is_multipart():
                for part in msg.walk():
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" in content_disposition:
                        attachment_path = self.save_attachment(part, email_id)
                        if attachment_path:
                            attachments.append(attachment_path)

            email_info = {
                "email_id": email_id,
                "subject": subject,
                "from": from_email,
                "to": to_email,
                "date": date,
                "body": body,
                "attachments": attachments
            }

            return email_info

        except Exception as e:
            print(f"处理邮件 {email_id} 失败: {str(e)}")
            return None

    def delete_email(self, email_id, folder='INBOX', expunge=True):
        try:
            self.client.select_folder(folder)
            self.client.set_flags(email_id, [b'\\Deleted'])
            # self.client.delete_messages(email_id)
            if expunge:
                self.client.expunge()
            print(f"成功删除 {len(email_id)} 封邮件")
            return True
        except Exception as e:
            print(f"删除邮件失败: {str(e)}")
            return False

    def logout(self):
        """退出登录"""
        if self.client:
            self.client.logout()
            print("已退出邮箱登录")


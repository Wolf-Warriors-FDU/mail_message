'''
Descripttion: your project
version: 1.0
Author: JiangFeng
Date: 2023-06-05 13:37:46
LastEditors: JiangFeng
LastEditTime: 2023-06-05 21:23:45
'''
import smtplib
import argparse
from email.mime.text import MIMEText
import sys
 

mail_host = 'smtp.qq.com' # QQ邮箱提供的SMTP服务器
port = 465 # 服务器端口，465或者587


def send_email(send_by, password, send_to, subject, message, send_self=False):
    send_to = send_by if send_self else send_to
    message = MIMEText(message,'plain','utf-8')
    message["From"] = send_by
    message['To'] = send_to
    message['Subject'] = subject
    # try:
    smpt = smtplib.SMTP_SSL(mail_host, port, 'utf-8')
    smpt.login(send_by,password)
    smpt.sendmail(send_by, send_to, message.as_string())
    print("Success!")
    # except:
    #     print("Fail")


def get_arg():
    parser = argparse.ArgumentParser(description='An simple tool for easy AI training.')
    parser.add_argument('--send_by', help='your qq email', type=str,
                        default="1308093945@qq.com")
    parser.add_argument('--send_to', help='target email address', type=str,
                        required=True)
    parser.add_argument('--password', help='your authorization code, and you can change the default for easy use.', 
                        default="", type=str)
    parser.add_argument('--subject', help='subject of your email', type=str, default="Test")
    parser.add_argument('--message', help='message of your email', type=str, default="Hello World.")
    args = parser.parse_args()
    return args


def main():
    args = get_arg()
    send_by = args.send_by
    password = args.password
    send_to = args.send_to
    subject = args.subject
    message = args.message
    send_email(send_by, password, send_to, subject,message, True)
    send_email(send_by, password, send_to, subject,message, False)


if __name__ == "__main__":
    main()